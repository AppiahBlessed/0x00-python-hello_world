#!/usr/bin/python3
'''
    This script emphasizes string substitution
'''
# Importing modules

import MySQLdb
import sys
if __name__ == "__main__":
    # Getting arguments passed
    user_n, pswd, dbname = sys.argv[1], sys.argv[2], sys.argv[3] 

    # Create connection
    connection = MySQLdb.connect(host='localhost', port=3306, user=user_n, passwd=pswd, db=dbname)

    # Get the cursor
    curs = connection.cursor()

    # Execute query
    curs.execute("SELECT * FROM states JOIN cities ON states.id = cities.state_id ORDER BY states.id ASC;")
    # Display results
    results= curs.fetchall()
    for result in results:
        print(f"({result[2]}, '{result[4]}', {result[1]})")
    # Close connection and cursor
    curs.close()
    connection.close()
