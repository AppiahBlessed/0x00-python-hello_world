#!/usr/bin/python3
'''
    This script filters the output
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
    curs.execute("SELECT * FROM states WHERE SUBSTRING(name, 1, 1) = 'N' ORDER BY id ASC;")

    # Display results
    results= curs.fetchall()
    for result in results:
        print(f"({result[0]}, '{result[1]}')")
