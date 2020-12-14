#!/usr/bin/python3
"""
Script that takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
It should be safe from MySQL injections
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    database = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    c = database.cursor()
    c.execute(
        "SELECT * "
        "FROM states WHERE name = %s ORDER BY states.id ASC", (argv[4], )
    )
    query_rows = c.fetchall()
    for row in query_rows:
        print(row)
    c.close()
    database.close()
