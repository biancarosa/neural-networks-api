from flask import Flask
from flask_mongoengine import MongoEngine
import os
app = Flask(__name__)

app.config.from_pyfile('config.cfg')
if os.environ.get('MONGODB_URI'):
    app.config['MONGODB_SETTINGS']['host'] = os.environ['MONGODB_URI']

db = MongoEngine(app)

import api.routes.hello_world
import api.routes.classification
