


import mysql.connector
from mysql.connector.cursor import MySQLCursorPrepared #new
cnx = mysql.connector.connect(user='brandon', password='lowery',
                              host='104.198.251.11',
                              database='data')


class database_update():

    def __init__(self, name):
        self.car_count = 0
        self.id = name


    def get_count(self):
        cursor = cnx.cursor(cursor_class=MySQLCursorPrepared) #new

        cursor = cnx.cursor(prepared=True) #new
        cursor = cnx.cursor(buffered=True)
        query = ("SELECT car_count FROM LOT_INFO WHERE lot_name = %s")

        #cursor.execute(query, ("kom",))
        cursor.execute(query, (self.id,))
        #return self.car_count
        for row in cursor:
            count = row

        cursor.close()
        cnx.close()


        return count

    def get_id(self):
        return self.id

    def add(self):
        self.car_count += 1

    def sub(self):
        self.car_count -= 1

kom = database_update("kom") #creates a db_update object named kom


kom.add() #adds one to the count in the db for kom

x = kom.get_count() #gives you kom lot count

print(x)
k = kom.get_id()
print(k)
