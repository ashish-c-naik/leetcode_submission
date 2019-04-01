# Write your MySQL query statement below
Select max(Salary) as SecondHighestSalary from Employee
Where Salary <> (Select max(Salary) as Salary
from Employee) 