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
app.config['SECRET_KEY'] = 'secret key here'
auth = HTTPDigestAuth()

users = {
    "vcu": "rams"
}

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

@app.route('/', methods=['GET'])
@auth.login_required
def index():
    t0 = time.time()
    r = requests.get(url="https://pong455.herokuapp.com/", auth=HTTPDigestAuth('vcu','rams'))
    tf = time.time()
    pingpong_t = (tf-t0)*1000
    return jsonify({
        'pingpong_t': [pingpong_t]
    })

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'message':'Page Not Here'}), 404


@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({'message':'Something is Broke'}), 500
