from flask_app import app
from flask import render_template
import pandas as pd
import json


dataframe = pd.read_csv('ufo_data_nuforc.csv')


@app.route('/')
def index():
    return render_template('index.html')