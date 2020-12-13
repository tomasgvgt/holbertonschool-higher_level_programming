#!/usr/bin/python3
"""
script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    database = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    c = database.cursor()
    c.execute(
        "SELECT id, name "
        "FROM states WHERE name like 'N%' ORDER BY states.id ASC"
        )
    query_rows = c.fetchall()
    for row in query_rows:
        print(row)
    c.close()
    database.close()
