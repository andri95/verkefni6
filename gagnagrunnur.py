from sys import argv

import bottle
from bottle import *
import pymysql.cursors

bottle.debug(True)

@get('/')
def index():
    connection = pymysql.connect(host='0106952799_verk7@localhost',
                                 user='user',
                                 password='passwd',
                                 db='db',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `user` (`user`, `pass`) VALUES (%s, %s)"
            cursor.execute(sql, ('andri', '5678'))

        connection.commit()

        with connection.cursor() as cursor:
            sql = "SELECT `user`, `pass` FROM `user` WHERE `user`=%s"
            cursor.execute(sql, ('andri',))
            result = cursor.fetchone()
            print(result)
    finally:
        connection.close()

bottle.run(host='0.0.0.0', port=argv[1])