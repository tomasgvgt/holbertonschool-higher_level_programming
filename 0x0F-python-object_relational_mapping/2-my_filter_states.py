#!/usr/bin/python3
"""
script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":

    database = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    c = database.cursor()
    c.execute(
        "SELECT id, name "
        "FROM states ORDER BY states.id ASC"
    )
    query_rows = c.fetchall()
    for row in query_rows:
        if row[1] == argv[4]:
            print(row)
    c.close()
    database.close()
