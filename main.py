# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 08:14:33 2021

@author: gianm
"""

#%%
import dataset
import pandas as pd

#%%
github_data = dataset.download_data('github')

#%%
dataset.load_to_hdfs(github_data)

#%%
df = pd.read_csv('Dataset/vaccinations-by-manufacturer.csv')
df.drop(columns=['Unnamed: 0'], inplace=True)

#%% get distinct
def get_distinct(df, column):
    location = df[column].drop_duplicates()
    return location

#%% date processing
from datetime import datetime
import calendar

def get_dow(date):
    datetime_obj = datetime.strptime(date, '%Y-%m-%d')
    return calendar.day_name[datetime_obj.weekday()]

def get_week(date):
    datetime_obj = datetime.strptime(date, '%Y-%m-%d')
    return datetime_obj.isocalendar()[1]

def get_month(date):
    datetime_obj = datetime.strptime(date, '%Y-%m-%d')
    return datetime_obj.month

def get_year(date):
    datetime_obj = datetime.strptime(date, '%Y-%m-%d')
    return datetime_obj.year

#%% 
dow = [get_dow(date) for date in df['date']]
week = [get_week(date) for date in df['date']]
month = [get_month(date) for date in df['date']]
year = [get_year(date) for date in df['date']]

df['dow'] = dow
df['week'] = week
df['month'] = month
df['year'] = year
