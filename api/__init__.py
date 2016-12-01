from flask import Flask
from flask_mongoengine import MongoEngine
import os
app = Flask(__name__)

app.config.from_pyfile('config.cfg')
if os.environ.get('ENV') == 'production':
    app.config['MONGODB_SETTINGS'] = {
        'db': str(os.environ['MONGODB_DB']),
        'username': str(os.environ['MONGODB_USERNAME']),
        'password': str(os.environ['MONGODB_PASSWORD']),
        'host': str(os.environ['MONGODB_HOST']),
        'port': int(os.environ['MONGODB_PORT'])
    }
db = MongoEngine(app)

import api.routes.hello_world
import api.routes.classification
