from flask import Flask, render_template, request
from flask import jsonify

from flask import Response

from os import listdir

import pandas as pd

# set tf backend to allow memory to grow, instead of claiming everything
#import tensorflow as tf

app = Flask(__name__, template_folder='template')
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/')
def index():
    return render_template('olap.html')

if __name__ == '__main__':

    app.run(host='0.0.0.0', port='80')
