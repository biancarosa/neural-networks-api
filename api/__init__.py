from flask import Flask

app = Flask(__name__)

import api.routes.hello_world
import api.routes.classification
