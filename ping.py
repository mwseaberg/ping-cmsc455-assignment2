import os
from flask import Flask, render_template, session, redirect, url_for, jsonify
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
import time
from flask_httpauth import HTTPDigestAuth
import requests

app = Flask(__name__)
auth = HTTPDigestAuth()

@app.route('/', methods=['GET'])
def index():
    t0 = time.time()
    r = requests.get(url="https://pong455.herokuapp.com/")
    data = r.json()
    print(data)
    tf = time.time()
    pingpong_t = (tf-t0)*1000
    return jsonify({
        'pingpong_t': [pingpong_t]
    })

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
