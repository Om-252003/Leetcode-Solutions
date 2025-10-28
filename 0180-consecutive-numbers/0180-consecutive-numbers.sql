# Write your MySQL query statement below
with cte as (
    select *,
    lead(num,1) over() as num2,
    lead(num,2) over() as num3
    from logs
)

select distinct num as consecutivenums
from cte
where num=num2
and num2=num3