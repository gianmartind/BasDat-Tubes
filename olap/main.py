from flask import Flask, render_template, request
from flask import jsonify

from flask import Response

from os import listdir

import pandas as pd
import plotly.express as px

import numpy as np

# set tf backend to allow memory to grow, instead of claiming everything
#import tensorflow as tf

app = Flask(__name__, template_folder='template')
app.config['TEMPLATES_AUTO_RELOAD'] = True

df_vaccinations = pd.DataFrame();
df_death_percent = pd.DataFrame();
df_covid_cases = pd.DataFrame();

@app.route('/')
def index():
    return render_template('olap.html')

@app.route('/chart1')
def chart1():
    global df_covid_cases
    df_covid_cases = pd.read_csv('daily_covid_cases.csv', header=None, names=['loc', 'date', 'week', 'month', 'val'])
    df_covid_cases['week'] = np.where((df_covid_cases.week == 53), 0, df_covid_cases.week)
    agg = request.args.get('agg')
    result_data = pd.DataFrame();
    if agg == 'date':
        result_data = df_covid_cases[['loc', 'date', 'val']]
    elif agg == 'week':
        result_data = df_covid_cases.groupby(['loc', 'week']).agg({'val':'sum'})
        result_data = result_data.reset_index()
    elif agg == 'month':
        result_data = df_covid_cases.groupby(['loc', 'month']).agg({'val':'sum'})
        result_data = result_data.reset_index()

    
    result_data_group = result_data.groupby('loc')
    result_dict = dict()
    for i in result_data_group.groups.keys():
        result_value = dict()
        result_value['period'] = result_data_group.get_group(i).iloc[:,1].to_list()
        result_value['val'] = result_data_group.get_group(i).iloc[:,2].to_list()

        result_dict[i] = result_value
    return jsonify(result_dict)

@app.route('/chart2')
def chart2():
    global df_vaccinations
    df_vaccinations = pd.read_csv('daily_vaccinations.csv', header=None, names=['loc', 'date', 'week', 'month', 'val'])
    df_vaccinations['week'] = np.where((df_vaccinations.week == 53), 0, df_vaccinations.week)
    agg = request.args.get('agg')
    result_data = pd.DataFrame();
    if agg == 'date':
        result_data = df_vaccinations[['loc', 'date', 'val']]
    elif agg == 'week':
        result_data = df_vaccinations.groupby(['loc', 'week']).agg({'val':'sum'})
        result_data = result_data.reset_index()
    elif agg == 'month':
        result_data = df_vaccinations.groupby(['loc', 'month']).agg({'val':'sum'})
        result_data = result_data.reset_index()

    
    result_data_group = result_data.groupby('loc')
    result_dict = dict()
    for i in result_data_group.groups.keys():
        result_value = dict()
        result_value['period'] = result_data_group.get_group(i).iloc[:,1].to_list()
        result_value['val'] = result_data_group.get_group(i).iloc[:,2].to_list()

        result_dict[i] = result_value
    return jsonify(result_dict)

@app.route('/chart3')
def chart3():
    global df_death_percent
    df_death_percent = pd.read_csv('daily_death_percent.csv', header=None, names=['loc', 'date', 'week', 'month', 'val'])
    df_death_percent['week'] = np.where((df_death_percent.week == 53), 0, df_death_percent.week)
    agg = request.args.get('agg')
    result_data = pd.DataFrame();
    if agg == 'date':
        result_data = df_death_percent[['loc', 'date', 'val']]
    elif agg == 'week':
        result_data = df_death_percent.groupby(['loc', 'week']).agg({'val':'sum'})
        result_data = result_data.reset_index()
    elif agg == 'month':
        result_data = df_death_percent.groupby(['loc', 'month']).agg({'val':'sum'})
        result_data = result_data.reset_index()

    
    result_data_group = result_data.groupby('loc')
    result_dict = dict()
    for i in result_data_group.groups.keys():
        result_value = dict()
        result_value['period'] = result_data_group.get_group(i).iloc[:,1].to_list()
        result_value['val'] = result_data_group.get_group(i).iloc[:,2].to_list()

        result_dict[i] = result_value
    return jsonify(result_dict)

if __name__ == '__main__':

    app.run(host='0.0.0.0', port='80')
