create database news;

DROP TABLE IF EXISTS articles;

CREATE TABLE articles (
    id SERIAL PRIMARY KEY,
    urlhash VARCHAR,
    urls VARCHAR,
    title VARCHAR,
    content TEXT,
    tag VARCHAR,
    published_date TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);