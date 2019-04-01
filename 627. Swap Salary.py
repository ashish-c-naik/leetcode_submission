# Write your MySQL query statement below
Update salary
SET sex = Case
                When sex = 'm' then 'f'
                else 'm'
            end
