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

The script printshe retrieved data, demonstrating a successful connection to the MySQL database
==============================================================================
==============================================================================

SUBSTRING Usage
In SQL, the SUBSTRING function is used to extract a substring from a string. It allows you to specify the starting position and the length of the substring to be extracted. The basic syntax is as follows:

sql
Copy code
SUBSTRING(string_expression, start_position, length)
string_expression: The source string from which the substring will be extracted.
start_position: The position within the string_expression where the extraction will begin. The first character is at position 1.
length: (Optional) The number of characters to be extracted. If omitted, the substring includes all characters from start_position to the end of the string.
Example Usage in the Script
In the provided script, the SUBSTRING function is utilized in the SQL query to filter the results based on the first letter of the "name" column:

sql
Copy code
curs.execute("SELECT * FROM states WHERE SUBSTRING(name, 1, 1) = 'N' ORDER BY id ASC;")
This query selects all rows from the "states" table where the first letter of the "name" column is 'N'. Here's a breakdown:

SUBSTRING(name, 1, 1): Extracts the first character of the "name" column.
= 'N': Compares the extracted character with the letter 'N'.
This allows for a specific filtering criterion based on the initial character of the "name" column



Script for Filtering States
This script utilizes string substitution to query the "states" table in the hbtn_0e_0_usa database. It takes four arguments—MySQL username, password, database name, and a state name to search. The results are sorted by states.id in ascending order, displaying matches with the specified state name..
