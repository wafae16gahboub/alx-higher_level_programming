#!/usr/bin/python3

if __name__ == "__main__":
    import MySQLdb
    import sys
    w = MySQLdb.connect(host="localhost",
                        port=3306,
                        user=sys.argv[1],
                        passwd=sys.argv[2],
                        db=sys.argv[3])
    cur = w.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY states.id ASC")
    g = cur.fetchall()
    for i in g:
        print(i)
    cur.close()
    w.close()
