import requests
import json
from flask import Flask

ecgapi = Flask(__name__)

@ecgapi.route('/')
def index():
    return 'API Coming Soon!'




