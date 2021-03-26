#!/usr/bin/env python3

"""
Write a script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
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
    cur.execute("SELECT cities.name "
                "FROM states JOIN cities ON "
                "states.id=cities.state_id "
                "WHERE states.name=%s ORDER BY cities.id", (argv[4], ))
    rows = cur.fetchall()
    # Print the first item of each row, separated by commas.
    print(", ".join(row[0] for row in rows))
