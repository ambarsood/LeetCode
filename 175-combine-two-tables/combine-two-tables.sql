# Write your MySQL query statement below
select P.firstName , P.lastNAme , A.city , A.state from Person P left join Address A on P.PersonId=A.PersonId;