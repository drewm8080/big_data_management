SELECT name AS Drinker FROM Drinkers WHERE name NOT IN (SELECT drinker FROM Frequents);

/* Output
Empty set (0.01 sec)
*/
