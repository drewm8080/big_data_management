SELECT distinct e.first_name, e.last_name FROM employees e INNER JOIN salaries s ON s.emp_no=e.emp_no WHERE s.salary>= 150000;

/* Output
+--------+
| emp_no |
+--------+
|  16021 |
|  21756 |
|  52983 |
|  73998 |
|  78783 |
|  88698 |
| 101753 |
| 216534 |
| 263268 |
| 410311 |
| 423386 |
| 459548 |
| 491899 |
+--------+
13 rows in set (0.15 sec)
*/