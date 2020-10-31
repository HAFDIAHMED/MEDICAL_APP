import argparse
import os
from flask import Flask
from flask_cors import CORS
from flask_restplus import Api
from flask_socketio import SocketIO

import shifaa.db.core as core
from shifaa.web.apis import NAMESPACES

VERSION = 1

# We define the base app that well be used to get the metrics :)
app = Flask(__name__)
socket = SocketIO(app)
CORS(app)
api = Api(app, prefix=f'/api/v{VERSION}')

for ns in NAMESPACES:
    api.add_namespace(ns)

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--debug', action='store_true', help='Use the server as a debug server')
    args = arg_parser.parse_args()

    debug = (os.getenv('SHIFAA_ENV', 'live') == 'dev') or args.debug
    # TODO : Move self to wsgi server

    # TODO : Ensure that we use the right tool of db migration
    #  to ensure that prod migration are automatic
    if debug:
        host, port = '0.0.0.0', 5000
    else:
        host, port = '0.0.0.0', 80
    core.setup_db()
    socket.run(host, port=port, debug=True)
