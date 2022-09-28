import os
from flask import Flask, jsonify 
import time

# basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    t0 = time.time()
    return str(t0)

