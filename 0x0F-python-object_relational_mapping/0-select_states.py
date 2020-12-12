#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    database = MySQLdb.connect(
        host="localhost", port=3306, user=sys.argv[1],
        passwd=sys.argv[2], db=sys.argv[3])
    c = database.cursor()
    c.execute("""SELECT id, name FROM states ORDER BY states.id ASC;""")
    query_rows = c.fetchall()
    for row in query_rows:
        print(row)
    c.close()
    database.close()
