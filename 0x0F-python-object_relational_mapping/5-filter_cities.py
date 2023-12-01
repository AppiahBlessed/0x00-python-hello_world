#!/usr/bin/python3
'''
    This script emphasizes Relational Databases
'''
# Importing modules

import MySQLdb
import sys
if __name__ == "__main__":
    # Getting arguments passed
    user_n, pswd, dbname, param = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    # Create connection
    connection = MySQLdb.connect(host='localhost', port=3306, user=user_n, passwd=pswd, db=dbname)

    # Get the cursor
    curs = connection.cursor()

    # Execute query
    curs.execute("""
            SELECT  cities.id, states.name, cities.name
            FROM cities JOIN states ON cities.state_id = states.id
            WHERE states.name = %s ORDER BY cities.id ASC;
        """, (param,))
    # Display results
    results= curs.fetchall()
    for index, result in enumerate(results):
        if (index == len(results) - 1):
            print(f"{result[2]}")
        else:
            print(f"{result[2]}, ", end='')
    # Close connection and cursor
    curs.close()
    connection.close()
