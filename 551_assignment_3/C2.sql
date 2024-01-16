SELECT Manufacturer,AVG(Price) AS Average FROM Beers2Bars GROUP BY Manufacturer;


/* Output
+----------------+---------+
| Manufacturer   | Average |
+----------------+---------+
| Anheuser-Busch |       3 |
| Heineken       |       2 |
| Pete's         |     3.5 |
+----------------+---------+
3 rows in set (0.00 sec)
*/