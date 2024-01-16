SELECT dept_no FROM dept_manager GROUP BY dept_no HAVING COUNT(emp_no) >=3;

/* Output
+---------+
| dept_no |
+---------+
| d004    |
| d006    |
| d009    |
+---------+
3 rows in set (0.00 sec)
*/