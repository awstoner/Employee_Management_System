CREATE DATABASE EmployeeManagement_DB
GO
USE EmployeeManagement_DB;
GO
-- ------------- CREATE STRUCTURE ------------- --
CREATE TABLE employee (
	id INT IDENTITY PRIMARY KEY,
	first_name VARCHAR (50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    age INT,
    salary INT NOT NULL,
    department_id INT NOT NULL,
    FOREIGN KEY (department_id) REFERENCES department(id),
    manager_id INT NOT NULL
    FOREIGN KEY (manager_id) REFERENCES employee(id)
);

CREATE TABLE address (
	id INT IDENTITY PRIMARY KEY,
	street VARCHAR (75),
	city VARCHAR(25) NOT NULL,
    state CHAR(2) NOT NULL,
);

CREATE TABLE department (
	id INT IDENTITY PRIMARY KEY,
    name VARCHAR(25) NOT NULL,
    manager_id INT NOT NULL,
    headquarters_address_id INT NOT NULL,
);