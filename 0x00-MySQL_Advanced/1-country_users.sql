-- Create table users if not exists with id, email, name, and country columns

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT,
    email varchar(255) NOT NULL UNIQUE,
    name varchar(255),
    country ENUM('US', 'CO', 'TN') DEFAULT 'US',
    PRIMARY KEY (id)
);
