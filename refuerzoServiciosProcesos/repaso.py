from sys import prefix

from flask import Flask

pepito = Flask(__name__)

pepito.register_blueprint(CountriesBP, prefix='/countries')