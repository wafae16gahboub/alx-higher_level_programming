#!/usr/bin/python3
"""script that takes in an argument and displays where name matches"""
import MySQLdb
import sys


def detectme():

    argvv = sys.argv
    n = MySQLdb.connect(user=argvv[1],
                        host='localhost',
                        port=3306,
                        passwd=argvv[2],
                        db=argvv[3])

    veronic = n.cursor()
    sec = "SELECT*FROM states WHERE BINARY name= %s ORDER BY id ASC"
    veronic.execute(sec, (argvv[4],))
    hussa = veronic.fetchall()
    for i in hussa:
        print(i)
    n.close()


if __name__ == "__main__":
    detectme()
