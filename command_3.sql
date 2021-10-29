SELECT
DISTINCT department.name,
SUM(employees.salary) OVER (PARTITION BY employees.department_id)
FROM employees
INNER JOIN department ON employees.department_id=department.id