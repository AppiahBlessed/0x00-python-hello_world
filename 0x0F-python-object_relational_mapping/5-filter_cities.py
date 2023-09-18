#!/usr/bin/python3
"""
 This is a pytthon script that takes in the
 name of a state as an argument and lists all
 cities of that state, using the database hbtn_0e_4_usa
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
        # Execute query
        cursor.execute("""SELECT cities.name FROM
                        cities INNER JOIN states
                        ON states.id=cities.state_id
                        WHERE states.name=%s""", (state_name,))

        # Display results
        output = cursor.fetchall()
        # Get the individual rows
        tmp = list(row[0] for row in output)
        print(*tmp, sep=", ")
# Module should not automatically run when imported
if __name__ == "__main__":
    main()
