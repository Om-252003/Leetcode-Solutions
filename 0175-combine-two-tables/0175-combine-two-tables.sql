select P.firstName, p.lastName, A.city, A.state
from Person p
left join Address A
on p.personId = a.personId
group by p.personId;