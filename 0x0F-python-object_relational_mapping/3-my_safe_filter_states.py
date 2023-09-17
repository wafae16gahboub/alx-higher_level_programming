#!/usr/bin/python3

if __name__ == "__main__":
    import MySQLdb
    import sys
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    arg4 = sys.argv[4]
    cur.execute("SELECT  id, name\
                FROM states\
                WHERE name LIKE %s\
                ORDER BY states.id ASC", (arg4,))
    query = cur.fetchall()
    for row in query:
        print(row)
    cur.close()
    db.close()
