/*
Suppose that a website contains two tables, the Customers table and the Orders table. Write a SQL query to find all customers who never order anything.

Table: Customers.

+----+-------+
| Id | Name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+
Table: Orders.

+----+------------+
| Id | CustomerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+
Using the above tables as example, return the following:

+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+
*/
-- 1st attempt: 68th percentile
--  Write your MySQL query statement below
SELECT name AS Customers
    FROM customers t1
        LEFT JOIN orders t2 on t1.id=t2.customerid
WHERE customerid IS NULL


-- 2nd attempt:80th percetnile in speed. clearer. like the lower case syntax.
--  Write your MySQL query statement below
select name as "Customers"
from customers
where Customers.id not in 
    (select distinct customerid from orders)


