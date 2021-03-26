#!/usr/bin/env python3

"""
script that lists all cities from the database hbtn_0e_4_usa
Using MySQLdb
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
    cur.execute("SELECT cities.id, cities.name, states.name "
                "FROM states JOIN cities ON "
                "states.id=cities.state_id ORDER BY cities.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
