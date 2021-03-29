#!/usr/bin/python3

"""
script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306, user=argv[1],
        password=argv[2],
        database=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE states.name like 'N%'"
                "ORDER BY states.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    c.close()
