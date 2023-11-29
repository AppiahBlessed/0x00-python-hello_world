#!/usr/bin/python3
'''
    This script lists all states from a database
'''
# Importing modules

import MySQLdb
import sys

# Getting arguments passed
user_n, pswd, dbname = sys.argv[1], sys.argv[2], sys.argv[3] 

# Create connection
connection = MySQLdb.connect(host='localhost', port=3306, user=user_n, passwd=pswd, db=dbname)

# Get the cursor
curs = connection.cursor()

# Execute query
curs.execute("SELECT * FROM states ORDER BY id ASC;")

# Display results
results= curs.fetchall()
for result in results:
    print(f"({result[0]}, '{result[1]}')")
