SELECT bar as Bar, COUNT(price) as Total FROM Sells WHERE price >=2 GROUP BY bar;


/* Output
+------------+-------+
| Bar        | Total |
+------------+-------+
| Bob's bar  |     2 |
| Joe's bar  |     4 |
| Mary's bar |     2 |
+------------+-------+
3 rows in set (0.00 sec)
*/