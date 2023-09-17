#!/usr/bin/python3
"""
 This is a python file that handles database
 operations using MYSQLdb
"""


def main():
    import sys
    import MySQLdb

    # Get command line argument passed
    u = sys.argv[1]
    pd = sys.argv[2]
    db_name = sys.argv[3]

    # Establish the connection
    with MySQLdb.connect(host='localhost', port=3306, user=u, password=pd,
                         db=db_name) as connect, connect.cursor() as cursor:
        # Execute query
        cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

        # Display results
        output = cursor.fetchall()
        for i in output:
            print(f"({i[0]}, '{i[1]}')")


# Module should not automatically run when imported
if __name__ == "__main__":
    main()
