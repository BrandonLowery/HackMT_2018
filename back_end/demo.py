#demo.py for simple demo


import mysql.connector
from mysql.connector.cursor import MySQLCursorPrepared

#cnx = mysql.connector.connect(user='brandon', password='lowery',
                            #  host='104.198.251.11',
                             # database='data')
#cursor = cnx.cursor(cursor_class=MySQLCursorPrepared)

#cursor = cnx.cursor(prepared=True)
#cursor = cnx.cursor(buffered=True)

import sched, time
#s = sched.scheduler(time.time, time.sleep)
#def do_something(sc):
while(True):
    cnx = mysql.connector.connect(user='brandon', password='lowery',
                                  host='104.198.251.11',
                                  database='data')
    cursor = cnx.cursor(cursor_class=MySQLCursorPrepared)

    cursor = cnx.cursor(prepared=True)
    cursor = cnx.cursor(buffered=True)
    #cursor = cnx.cursor(cursor_class=MySQLCursorPrepared)

    #cursor = cnx.cursor(prepared=True)
    #cursor = cnx.cursor(buffered=True)
    print "Cars currently in lot:"
    query = ("SELECT car_count FROM LOT_INFO WHERE lot_name = %s")
    cursor.execute(query, ("kom",))

    for row in cursor:
        t= str(row)
        t = t[1:-2]
        print(t)
    cursor.close()
    cnx.close()
    #execfile('Tracker.py')
    time.sleep(2)


    #s.enter(2, 1, do_something, (sc,))

#s.enter(2, 1, do_something, (s,))
#s.run()
