CREATE VIEW Beers2Bars AS SELECT b.manf AS Manufacturer, s.beer AS Beer, s.bar AS Bar, s.price AS Price FROM Sells s INNER JOIN Beers b ON b.name = s.beer;

/* Output
PLEASE NOTE: I had already had created the table
ERROR 1050 (42S01): Table 'Beers2Bars' already exists
*/