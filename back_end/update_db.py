


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
        #cnx.close()


        return count

    def get_id(self):
        return self.id

    def add(self):
        self.car_count += 1
        cursor = cnx.cursor(cursor_class=MySQLCursorPrepared) #new

        cursor = cnx.cursor(prepared=True) #new
        cursor = cnx.cursor(buffered=True)
        query = "UPDATE LOT_INFO SET car_count = (%s) WHERE lot_name = (%s)"
        cursor.execute(query, (self.car_count,"kom"))
        cursor.close()
    def sub(self):
        self.car_count -= 1
        cursor = cnx.cursor(cursor_class=MySQLCursorPrepared) #new

        cursor = cnx.cursor(prepared=True) #new
        cursor = cnx.cursor(buffered=True)
        query = "UPDATE LOT_INFO SET car_count = (%s) WHERE lot_name = (%s)"
        cursor.execute(query, (self.car_count,"kom"))
        cursor.close()
