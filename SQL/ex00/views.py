from django.http import HttpResponse
from django.conf import settings
import psycopg2

# Create your views here.
def init(request):
    db_config = settings.DATABASES['default']
    conn = None
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
                CREATE TABLE IF NOT EXISTS ex00_movies (
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
