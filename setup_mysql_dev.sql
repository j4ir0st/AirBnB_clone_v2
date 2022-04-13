-- A database hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- A new user hbnb_dev (in localhost)
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost';
-- The password of hbnb_dev should be set to hbnb_dev_pwd
SET PASSWORD FOR 'hbnb_dev'@'localhost' = 'hbnb_dev_pwd';

USE hbnb_dev_db;
-- hbnb_dev should have all privileges on the database hbnb_dev_db (and only this database)
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- hbnb_dev should have SELECT privilege on the database performance_schema (and only this database)
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
