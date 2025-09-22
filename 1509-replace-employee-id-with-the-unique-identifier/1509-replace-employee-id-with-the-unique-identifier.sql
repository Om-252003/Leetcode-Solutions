# Write your MySQL query statement below
select eu.unique_id, e.name
from Employees e
left join EmployeeUNI eu
on e.id = eu.id;

/* SELECT 
    eu.unique_id,
    e.name
FROM Employees e
LEFT JOIN EmployeeUNI eu
    ON e.id = eu.id*/
