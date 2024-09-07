CREATE DATABASE tasks;
CREATE USER batman WITH PASSWORD '123456';
ALTER ROLE batman SET client_encoding TO 'utf8';
ALTER ROLE batman SET default_transaction_isolation TO 'read committed';
ALTER ROLE batman SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE tasks TO batman;
