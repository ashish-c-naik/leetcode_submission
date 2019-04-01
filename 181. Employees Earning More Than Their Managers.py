SELECT newTable.Name as "Employee"
FROM (
SELECT A.Name, A.Salary, A.ManagerId, B.Salary as "MSalary"
FROM Employee as A, Employee as B
WHERE A.ManagerId = B.Id ) as newTable
WHERE newTable.Salary > newTable.MSalary