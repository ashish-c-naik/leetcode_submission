# Write your MySQL query statement below
Select w.Id
FROM Weather as w, Weather as s
WHERE DATEDIFF(w.RecordDate, s.RecordDate)=1 AND w.Temperature > s.Temperature