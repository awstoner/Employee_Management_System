-- Command #1
-- Returns full data for each Employee with their address as a string, department name, and manager name
SELECT 
employees.id,
employees.name,
employees.age,
employees.salary,
address.street || address.city || ',' || address.state as 'full_address',
department.name as 'department_name'
FROM employees
INNER JOIN department ON employees.department_id=department.id
INNER JOIN address ON employees.address_id=address.id;


-- Command #2
-- Returns the 5 highest paid and lowest paid employees
SELECT name, salary
FROM employees
ORDER BY salary DESC LIMIT 5;

SELECT name, salary
FROM employees
ORDER BY salary ASC LIMIT 5;


-- Command #3 
-- Returns total salary for each department, the manager's name, sorted by highest total
SELECT DISTINCT department.name,
SUM(employees.salary) OVER (PARTITION BY employees.department_id) as department_total_salary, employees.name as manager_name
FROM employees
INNER JOIN department ON employees.id=department.manager_id;


-- Command #4
-- Returns each employee that lives in a given state
SELECT employees.name, address.state
FROM employees
LEFT JOIN address ON employees.address_id=address.id
WHERE address.state LIKE '%FL';
-- Change "WHERE" statement to search for specific state