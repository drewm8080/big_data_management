SELECT drinker FROM Likes WHERE beer NOT LIKE "Summerbrew" AND beer LIKE "%Bud%";


/* Output
+----------+
| drinker  |
+----------+
| Bill     |
| Jennifer |
| Steve    |
| Steve    |
+----------+
4 rows in set (0.00 sec)
*/