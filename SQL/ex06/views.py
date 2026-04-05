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
                CREATE TABLE IF NOT EXISTS ex06_movies (
                    title varchar(64) UNIQUE NOT NULL,
                    episode_nb int PRIMARY KEY,
                    opening_crawl text,
                    director varchar(32) NOT NULL,
                    producer varchar(128) NOT NULL,
                    release_date date NOT NULL,
                    created timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
                    updated timestamp with time zone DEFAULT CURRENT_TIMESTAMP
                )
                """)
                cur.execute("""
                CREATE OR REPLACE FUNCTION update_changetimestamp_column()
                RETURNS TRIGGER AS $$
                BEGIN
                NEW.updated = now();
                NEW.created = OLD.created;
                RETURN NEW;
                END;
                $$ language 'plpgsql';
                """)
                cur.execute("""
                CREATE TRIGGER update_films_changetimestamp BEFORE UPDATE
                ON ex06_movies FOR EACH ROW EXECUTE PROCEDURE
                update_changetimestamp_column();
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
                        INSERT INTO ex06_movies (episode_nb, title, director, producer, release_date)
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
                cur.execute("SELECT * FROM ex06_movies")
                movies = cur.fetchall()
                if not movies:
                    return HttpResponse("No data available.")
                return render(request, 'ex06/ex06_display.html', {'movies': movies})
    except Exception as e:
        return HttpResponse(f"Error: {e}")


def update(request):
    db_config = settings.DATABASES['default']
    try:
        conn = psycopg2.connect(
            dbname=db_config["NAME"],
            user=db_config["USER"],
            password=db_config["PASSWORD"],
            host=db_config["HOST"],
            port=db_config["PORT"]
        )
        with conn:
            with conn.cursor() as cur:
                if request.method == "POST":
                    title = request.POST.get("title")
                    opening_crawl = request.POST.get("opening_crawl")
                    print(title)
                    print(opening_crawl)
                    if title and opening_crawl:
                        cur.execute("UPDATE ex06_movies SET opening_crawl = %s WHERE title = %s", [opening_crawl, title])
                        conn.commit()

                cur.execute("SELECT title FROM ex06_movies")
                titles = [row[0] for row in cur.fetchall()]
                if not titles:
                    return HttpResponse("No data available.")
                return render(request, "ex06/ex06_update.html", {"titles": titles})
    except Exception as e:
        return HttpResponse(f"Error: {e}")
