#!/usr/bin/python3

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306, user=argv[1],
        password=argv[2],
        database=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE states.name =%s "
                "ORDER BY states.id", (argv[4], ))
    rows = cur.fetchall()
    for row in rows:
        print(row)
