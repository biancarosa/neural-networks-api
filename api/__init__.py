from flask import Flask
import mongoengine
import os
app = Flask(__name__)

app.config.from_pyfile('config.cfg')
if os.environ.get('ENV') == 'production':
    app.config['MONGODB_SETTINGS'] = {
        'host': os.environ['MONGODB_URI']
    }
mongoengine.connect(host=app.config['MONGODB_SETTINGS']['host'])

import api.routes.hello_world
import api.routes.classification
