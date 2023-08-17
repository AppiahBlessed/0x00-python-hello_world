How to Create a New MySQL User
To create a new MySQL user, you can use the CREATE USER statement. Here's an example:

sql
Copy code
CREATE USER 'username'@'hostname' IDENTIFIED BY 'password';
Replace 'username', 'hostname', and 'password' with the desired values. After creating the user, you can grant privileges using the GRANT statement.

How to Manage Privileges for a User to a Database or Table
To manage privileges for a user, use the GRANT and REVOKE statements. For example, to grant a user SELECT and INSERT privileges on a specific table:

sql
Copy code
GRANT SELECT, INSERT ON database_name.table_name TO 'username'@'hostname';
To revoke privileges:

sql
Copy code
REVOKE SELECT, INSERT ON database_name.table_name FROM 'username'@'hostname';
Whats a PRIMARY KEY
A PRIMARY KEY is a column or combination of columns in a table that uniquely identifies each row. It enforces the uniqueness constraint and provides a way to efficiently search and retrieve data from the table.

Whats a FOREIGN KEY
A FOREIGN KEY is a column that establishes a link between data in two tables. It creates a relationship between the tables, typically referencing the primary key of another table. This relationship ensures data integrity and consistency.

How to Use NOT NULL and UNIQUE Constraints
The NOT NULL constraint ensures that a column cannot have a NULL value. The UNIQUE constraint enforces that all values in a column are unique, preventing duplicate entries.

sql
Copy code
CREATE TABLE example (
    id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE
);
How to Retrieve Data from Multiple Tables in One Request
You can retrieve data from multiple tables using JOIN clauses. For example, an INNER JOIN combines matching rows from both tables based on a specified condition.

sql
Copy code
SELECT orders.order_id, customers.customer_name
FROM orders
INNER JOIN customers ON orders.customer_id = customers.customer_id;
What Are Subqueries
Subqueries are queries nested within other queries. They can be used in various parts of SQL statements, such as the SELECT, FROM, WHERE, and HAVING clauses, to retrieve data based on results from another query.

sql
Copy code
SELECT product_name
FROM products
WHERE category_id IN (SELECT category_id FROM categories WHERE category_name = 'Electronics');
What Are JOIN and UNION
JOIN: A JOIN combines rows from two or more tables based on a related column between them. Common types of JOINs include INNER JOIN, LEFT JOIN (or LEFT OUTER JOIN), RIGHT JOIN (or RIGHT OUTER JOIN), and FULL JOIN (or FULL OUTER JOIN).

UNION: A UNION combines the result sets of two or more SELECT statements into a single result set. It removes duplicates by default, while UNION ALL retains duplicates.

These are fundamental concepts in relational databases that allow you to work with data from multiple tables and create more complex queries.
