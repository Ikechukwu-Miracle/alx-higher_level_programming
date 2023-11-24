#!/usr/bin/python3
""" List all states from hbtn_0e_0_usa and prevents SQL injection """
import MySQLdb
import sys


if __name__ == "__main__":
	searchName = sys.argv[4]

    connection = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
	cur = connection.cursor()
	query = "SELECT * FROM states WHERE name = %s ORDER BY states.id ASC"
	cur.execute(query, (searchName,))
	results = cur.fetchall()

	for row in results:
		print(row)

	cur.close()
	connection.close()
