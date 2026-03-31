CREATE TABLE IF NOT EXISTS ex00_movies (
    title varchar(64) UNIQUE NOT NULL,
    episode_nb int PRIMARY KEY,
    opening_crawl text,
    director varchar(32) NOT NULL,
    producer varchar(128) NOT NULL,
    release_date date NOT NULL
)
