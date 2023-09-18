#!/usr/bin/python3
"""
 This is a pytthon script that
  lists all cities from the database hbtn_0e_4_usa
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
        cursor.execute("""SELECT cities.id, cities.name, states.name FROM
                        cities INNER JOIN states
                        ON states.id=cities.state_id""")

        # Display results
        output = cursor.fetchall()
        # Get the individual rows
        for i in output:
            print(i)


# Module should not automatically run when imported
if __name__ == "__main__":
    main()
