from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
import psycopg2
from psycopg2.extras import DictCursor
import os

# Create your views here.
def init(request):
    db_config = settings.DATABASES['default']
    try:
        conn = psycopg2.connect(
            dbname=db_config['NAME'],
            user=db_config['USER'],
            password=db_config['PASSWORD'],
            host=db_config['HOST'],
            port=db_config['PORT']
        )
        with conn:
            with conn.cursor() as cur:
                cur.execute("""
                CREATE TABLE IF NOT EXISTS ex08_planets (
                    id serial PRIMARY KEY,
                    name varchar(64) UNIQUE NOT NULL,
                    climate varchar(255),
                    diameter int,
                    orbital_period int,
                    population bigint,
                    rotation_period int,
                    surface_water real,
                    terrain varchar(128)
                )
                """)
                cur.execute("""
                CREATE TABLE IF NOT EXISTS ex08_people (
                    id serial PRIMARY KEY,
                    name varchar(64) UNIQUE NOT NULL,
                    birth_year varchar(32),
                    gender varchar(32),
                    eye_color varchar(32),
                    hair_color varchar(32),
                    height int,
                    mass real,
                    homeworld varchar(64) REFERENCES ex08_planets(name)
                )
                """)
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(f"Error: {e}")


def populate(request):
    db_config = settings.DATABASES['default']
    try:
        conn = psycopg2.connect(
            dbname=db_config['NAME'],
            user=db_config['USER'],
            password=db_config['PASSWORD'],
            host=db_config['HOST'],
            port=db_config['PORT']
        )
        planets_path = os.path.join(settings.BASE_DIR, 'planets.csv')
        people_path = os.path.join(settings.BASE_DIR, 'people.csv')
        results = []
        with conn:
            with conn.cursor() as cur:
                with open(planets_path, 'r') as f:
                    cur.copy_expert("""
                                    COPY ex08_planets(name, climate, diameter, orbital_period, population, rotation_period, surface_water, terrain)
                                    FROM STDIN WITH (FORMAT CSV, DELIMITER '\t', NULL 'NULL')""", f)
                results.append("OK.")
                with open(people_path, 'r') as f:
                    cur.copy_expert("""
                                    COPY ex08_people(name, birth_year, gender, eye_color, hair_color, height, mass, homeworld)
                                    FROM STDIN WITH (FORMAT CSV, DELIMITER '\t', NULL 'NULL')""", f)
                results.append("OK.")
        return HttpResponse(results)
    except Exception as e:
        return HttpResponse(f"Error: {e}")


def display(request):
    db_config = settings.DATABASES['default']
    try:
        conn = psycopg2.connect(
            dbname=db_config['NAME'],
            user=db_config['USER'],
            password=db_config['PASSWORD'],
            host=db_config['HOST'],
            port=db_config['PORT']
        )
        with conn:
            with conn.cursor(cursor_factory=DictCursor) as cur:
                cur.execute("""
                    SELECT people.name, people.homeworld, planets.climate 
                    FROM ex08_people people
                    JOIN ex08_planets planets
                    ON people.homeworld = planets.name
                    WHERE planets.climate LIKE '%windy%'
                    ORDER BY people.name ASC
                """)
                people = cur.fetchall()
                if not people:
                    return HttpResponse("No data available.")
                return render(request, 'ex08/ex08_display.html', {'people': people})
    except Exception as e:
        return HttpResponse(f"Error: {e}")
