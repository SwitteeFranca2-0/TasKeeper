-- this script prepares a Mysql database for the project
-- creates project deployment database wuth the name 'taskeeper_db'

CREATE DATABASE IF NOT EXISTS taskeeper_db;
CREATE USER IF NOT EXISTS 'taskeeper'@'localhost' IDENTIFIED BY 'taskeeper_pwd';
GRANT ALL PRIVILEGES ON taskeeper_db.* TO 'taskeeper'@'localhost';
FLUSH PRIVILEGES;
GRANT SELECT ON performance_schema.* TO 'taskeeper'@'localhost';
FLUSH PRIVILEGES;
