import re

from flask_cors import CORS

from app import app

regEx=re.compile(app.config['API_URL'] + "/*")
CORS(app, resources={regEx: {"origins": "*"}})
