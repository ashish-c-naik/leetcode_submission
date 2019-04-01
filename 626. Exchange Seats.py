# Write your MySQL query statement below
SELECT if(id<(select count(*) from seat),id+1,id) as id, student
FROM seat
WHERE id%2=1
UNION
SELECT id-1 as id, student
FROM seat
WHERE id%2=0
ORDER BY id 