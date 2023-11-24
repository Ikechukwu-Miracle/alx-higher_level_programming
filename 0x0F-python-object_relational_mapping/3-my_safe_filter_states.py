#!/usr/bin/python3
""" List all states from hbtn_0e_0_usa and prevents SQL injection """
import MySQLdb
import sys


if __name__ == "__main__":
	username, passwd = sys.argv[1], sys.argv[2]
	db_name, searchName = sys.argv[3], sys.argv[4]

    connection = MySQLdb.connect(host="localhost", port=3306,
            		user=username, passwd=passwd, db=db_name)
	cur = connection.cursor()
	query = "SELECT * FROM states WHERE name = %s ORDER BY states.id ASC"
	cur.execute(query, (searchName,))
	results = cur.fetchall()

	for row in results:
		print(row)

	cur.close()
	connection.close()
