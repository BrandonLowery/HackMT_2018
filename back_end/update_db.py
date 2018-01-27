


import mysql.connector
from mysql.connector.cursor import MySQLCursorPrepared #new



class  idk(object):

    cnx = mysql.connector.connect(user='brandon', password='lowery',
                                  host='104.198.251.11',
                                  database='data')


    def add_one(string):
        cursor = cnx.cursor(cursor_class=MySQLCursorPrepared) #new

        cursor = cnx.cursor(prepared=True) #new
        cursor = cnx.cursor(buffered=True)

        
