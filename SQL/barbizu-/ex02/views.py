from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
import psycopg2
from psycopg2.extras import DictCursor

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
                CREATE TABLE IF NOT EXISTS ex02_movies (
                    title varchar(64) UNIQUE NOT NULL,
                    episode_nb int PRIMARY KEY,
                    opening_crawl text,
                    director varchar(32) NOT NULL,
                    producer varchar(128) NOT NULL,
                    release_date date NOT NULL
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
        data = [
            (1, 'The Phantom Menace', 'George Lucas', 'Rick McCallum', '1999-05-19'),
            (2, 'Attack of the Clones', 'George Lucas', 'Rick McCallum', '2002-05-16'),
            (3, 'Revenge of the Sith', 'George Lucas', 'Rick McCallum', '2005-05-19'),
            (4, 'A New Hope', 'George Lucas', 'Gary Kurtz, Rick McCallum', '1977-05-25'),
            (5, 'The Empire Strikes Back', 'Irvin Kershner', 'Gary Kurtz, Rick McCallum', '1980-05-17'),
            (6, 'Return of the Jedi', 'Richard Marquand', 'Howard G. Kazanjian, George Lucas, Rick McCallum', '1983-05-25'),
            (7, 'The Force Awakens', 'J. J. Abrams', 'Kathleen Kennedy, J. J. Abrams, Bryan Burk', '2015-12-11')
        ]
        results = []
        with conn:
            with conn.cursor() as cur:
                try:
                    for movie in data:
                        cur.execute("""
                        INSERT INTO ex02_movies (episode_nb, title, director, producer, release_date)
                        VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING
                        """, movie)
                        results.append("OK.")
                except Exception as e:
                    conn.rollback()
                    return HttpResponse(f"Error: {e}")

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
                cur.execute("SELECT * FROM ex02_movies")
                movies = cur.fetchall()
                if not movies:
                    return HttpResponse("No data available.")
                return render(request, 'ex02/ex02_display.html', {'movies': movies})
    except Exception as e:
        return HttpResponse(f"Error: {e}")
