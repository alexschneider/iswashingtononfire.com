from flask import Flask, render_template
from get_and_parse_fire_page import get_fire_dict
import os
import sys
app = Flask(__name__)
app.config['SERVER_NAME'] = os.environ['SERVER_NAME']

@app.route('/')
def index():
    return render_template('isfire.html', **get_fire_dict())

@app.route('/', subdomain='www')
def www_index():
    return index()

@app.route('/', subdomain='where')
def where_index():
    return render_template('wherefire.html', **get_fire_dict())

@app.route('/', subdomain='howmuch')
def howmuch_index():
    fire_dict = get_fire_dict()
    fire_dict['totalacres'] = sum(int(fire['acres']) for fire in fire_dict['fires'])
    return render_template('howmuchfire.html', **fire_dict)