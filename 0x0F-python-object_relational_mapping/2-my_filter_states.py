#!/usr/bin/python3
"""
 This is a pytthon script that writes takes in an argument
 and displays all values in the states table of hbtn_0e_0_usa
 where name matches the argument.

"""


def main():
    import sys
    import MySQLdb

    # Get command line argument passed
    u = sys.argv[1]
    pd = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Establish the connection
    with MySQLdb.connect(host='localhost', port=3306, user=u, password=pd,
                         db=db_name) as connect, connect.cursor() as cursor:
        # Execute query using the format string
        cursor.execute("""SELECT * FROM states WHERE name
                        LIKE BINARY '{}'
                        ORDER BY states.id ASC""".format(state_name))

        # Display results
        output = cursor.fetchall()
        # Get all names that begin with capital N
        for i in output:
            print(i)


# Module should not automatically run when imported
if __name__ == "__main__":
    main()
