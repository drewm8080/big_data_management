SELECT bar as Bar FROM Sells WHERE price = (SELECT MAX(price) FROM Sells);


/* Output
+-----------+
| Bar       |
+-----------+
| Joe's bar |
+-----------+
1 row in set (0.00 sec)
*/