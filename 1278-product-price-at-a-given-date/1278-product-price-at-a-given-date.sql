WITH rank_CTE AS(
    SELECT *, RANK ()OVER(PARTITION BY product_id ORDER BY change_date desc) AS r
FROM Products
WHERE change_date<='2019-08-16')

SELECT product_id,new_price AS price
FROM rank_CTE
WHERE r=1
UNION
SELECT product_id,10 AS price
FROM Products
WHERE product_id NOT IN(SELECT product_id FROM rank_CTE)