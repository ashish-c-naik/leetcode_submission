# Write your MySQL query statement below
SELECT Name as Customers
FROM Customers
WHERE Id <> ALL(
SELECT CustomerId
FROM Orders
)