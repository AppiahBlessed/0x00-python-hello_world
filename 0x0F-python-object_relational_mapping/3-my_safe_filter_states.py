#!/usr/bin/python3
'''
    This script emphasizes string substitution
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
    curs.execute("SELECT * FROM states WHERE name=%s ORDER BY id ASC;", (param,))
    # Display results
    results= curs.fetchall()
    for result in results:
        print(f"({result[0]}, '{result[1]}')")

    # Close connection and cursor
    curs.close()
    connection.close()
