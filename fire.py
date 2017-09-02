from flask import Flask, render_template
from get_and_parse_fire_page import get_fire_dict
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('isfire.html', **get_fire_dict())

@app.route('/where')
def where():
    return render_template('wherefire.html', **get_fire_dict())