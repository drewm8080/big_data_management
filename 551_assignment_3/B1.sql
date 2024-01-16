SELECT manf FROM Beers GROUP BY manf HAVING COUNT(name) >=3;


/* Output
+----------------+
| manf           |
+----------------+
| Anheuser-Busch |
+----------------+
1 row in set (0.01 sec)
*/