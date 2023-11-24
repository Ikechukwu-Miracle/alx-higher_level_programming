#!/usr/bin/python3
"""List all states from hbtn_0e_0_usa and prevents SQL injection"""
import MySQLdb
import sys


def searchByNameSafe(username, passwd, db_name, searchName):
    """searches the database specified by db_name using the searchName.

    Args:
        username (str): the username of the MySQL server
        passwd (str): pasword
        db_name (str): database name
        searchName (str): Keyword used to search the database table
    """

    try:
        connection = MySQLdb.connect(host="localhost", port=3306, \
            user=username, passwd=passwd, db=db_name)
		cur = connection.cursor()
		query = "SELECT * FROM states WHERE name = %s ORDER BY states.id ASC"
		cur.execute(query, (searchName,))
		results = cur.fetchall()

		for row in results:
			print(row)

	except MySQLdb.Error as e:
		pass

	finally:
		if cur:
			cur.close()
		if connection:
			connection.close()


if __name__ == "__main__":
	username, passwd = sys.argv[1], sys.argv[2]
	db_name, searchName = sys.argv[3], sys.argv[4]

	searchByNameSafe(username, passwd, db_name, searchName)