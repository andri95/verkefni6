from sys import argv

import bottle
from bottle import *

bottle.debug(True)

@get('/')
def index():
    return "Hallo Heimur í Heroku og Github"

bottle.run(host='0.0.0.0', port=argv[1])