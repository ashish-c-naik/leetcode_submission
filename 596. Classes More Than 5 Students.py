# Write your MySQL query statement below
SELECT class
FROM courses
Group by class
HAVING COUNT(distinct student) >= 5