Connecting to MySQL
The script connects to the MySQL database using the MySQLdb library in Python. The connection process involves the following stages:

Importing Modules:

The necessary Python modules, including MySQLdb and sys, are imported at the beginning of the script.

Command Line Arguments:

The script retrieves MySQL credentials (username, password, database name) as command-line arguments.

Creating a Connection:

A connection to the MySQL database is established using the MySQLdb.connect() method.

Getting Cursor:

A cursor is obtained using the connection.cursor() method. The cursor allows executing SQL queries.

Executing Query:

An SQL query to select all records from the "states" table is executed using the cursor.execute() method.

Fetching Results:

The results of the query are fetched using cursor.fetchall(), and the script then iterates over the results.

Displaying Results:

The script prints the retrieved data, demonstrating a successful connection to the MySQL database
