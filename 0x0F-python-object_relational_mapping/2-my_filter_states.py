#!/usr/bin/python3
import MySQLdb
import sys
""" Scripts take in an argument and displays all values in the states table of hbtn_0e_0_usa where name
matches the argument. The script takes in 4 arguments: mysql username, mysql password, database name and state name
"""

if __name__ == "__main__":
    user, passwd, db_name, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=passwd,
        db=db_name,
        charset="utf8"
    )
    cursor = db.cursor()
    cursor.execute("""
    SELECT * FROM states WHERE name LIKE "{}" ORDER BY id ASC
    """ .format(state_name))
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()
