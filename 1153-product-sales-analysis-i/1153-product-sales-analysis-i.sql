# Write your MySQL query statement below
select p.product_name, s.year, s.price
from Product p
right join Sales s
on s.product_id = p.product_id;