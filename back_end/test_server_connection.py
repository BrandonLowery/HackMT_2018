import mysql.connector
from mysql.connector.cursor import MySQLCursorPrepared #new

cnx = mysql.connector.connect(user='brandon', password='lowery',
                              host='104.198.251.11',
                              database='data')


#cursor = cnx.cursor()
cursor = cnx.cursor(cursor_class=MySQLCursorPrepared) #new

cursor = cnx.cursor(prepared=True) #new
cursor = cnx.cursor(buffered=True)

k = 21
#x = "UPDATE LOT_INFO SET car_count = (%s) WHERE lot_name = (%s)"

#cursor.execute(x, (k,"kom"))
#cnx.commit()

query = ("SELECT car_count FROM LOT_INFO WHERE lot_name = %s")

cursor.execute(query, ("kom",))

#print(query)



for row in cursor:
    print(row)



cursor.close()
cnx.close()
