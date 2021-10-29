SELECT 
employees.id,
employees.name,
employees.age,
employees.salary,
address.street || address.city || ',' || address.state as 'full_address',
department.name as 'department_name'
FROM employees
INNER JOIN department ON employees.department_id=department.id
INNER JOIN address ON employees.address_id=address.id
