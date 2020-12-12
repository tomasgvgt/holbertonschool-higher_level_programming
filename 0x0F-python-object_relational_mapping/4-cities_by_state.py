#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    database = MySQLdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], db=argv[3])
    c = database.cursor()
    c.execute(
        "SELECT cities.id, cities.name, states.name "
        "FROM cities JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id ASC"
    )
    query_rows = c.fetchall()
    for row in query_rows:
        print(row)
    c.close()
    database.close()
