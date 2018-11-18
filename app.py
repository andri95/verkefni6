from sys import argv

import bottle
from bottle import *
import pymysql.cursors

bottle.debug(True)

@get('/')
def index():
    connection = pymysql.connect(host='localhost',
                                 user='user',
                                 password='passwd',
                                 db='db',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `user` (`name`) VALUES (%s)"
            cursor.execute(sql, ('Admin', 'Daníel Daníelsson'))

        connection.commit()

        with connection.cursor() as cursor:
            sql = "SELECT `user`, `pass` FROM `user` WHERE `name`=%s"
            cursor.execute(sql, ('webmaster@python.org',))
            result = cursor.fetchone()
            print(result)
    finally:
        connection.close()

bottle.run(host='0.0.0.0', port=argv[1])