# Write your MySQL query statement below
Delete From Person
Where Person.Id not in ( Select Id From(
Select MIN(Person.Id) as Id
FROM Person
Group by Email) as Small
)