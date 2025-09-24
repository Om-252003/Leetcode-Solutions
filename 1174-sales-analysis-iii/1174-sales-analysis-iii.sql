# Write your MySQL query statement below
select p.product_id, p.product_name
from  product p
join Sales s
on s.product_id = p.product_id
group by p.product_id, p.product_name
having min(s.sale_date) >= '2019-01-01' and
       max(s.sale_date) <= '2019-03-31'
