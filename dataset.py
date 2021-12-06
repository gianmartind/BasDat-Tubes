# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 10:00:43 2021

@author: gianm
"""

#%%
import pandas as pd
from hdfs import InsecureClient
import time

def download_data(src=None):
    if src == None:
        return None
    elif src == 'github':
        return download_github_data()
    elif src == 'gstatic':
        return download_gstatic_data()
        
def download_github_data():
    start_time = time.time()
    github_links = [
            'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv',
            'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations-by-manufacturer.csv',
            'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations-by-age-group.csv',
            'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv',
            'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/variants/covid-variants.csv'
        ]
    
    datasets_github = dict()
    
    for data in github_links:
        dataset_name = data.split('/')[-1].lower()
        datasets_github[dataset_name] = pd.read_csv(data)
        print('\'{}\' downloaded'.format(dataset_name))
    
    print('Time taken: {}s'.format(round(time.time() - start_time, 2)))
    return datasets_github

def download_gstatic_data():
    start_time = time.time()
    gstatic_links = ['https://www.gstatic.com/covid19/mobility/Global_Mobility_Report.csv']
    
    datasets_gstatic = dict()
    
    for data in gstatic_links:
        dataset_name = data.split('/')[-1].lower()
        datasets_gstatic[dataset_name] = pd.read_csv(data)
        print('\'{}\' downloaded'.format(dataset_name))

    
    print('Time taken: {}s'.format(round(time.time() - start_time, 2)))
    return datasets_gstatic

def load_to_hdfs(datasets):
    start_time = time.time()
    client_hdfs = InsecureClient('http://localhost:9870')
    
    for data in datasets.keys():
        with client_hdfs.write('/basdatpbd/tubes/{}'.format(data), encoding='utf-8') as writer:
            datasets[data].to_csv(writer, index=False)
        print('\'{}\' loaded to hdfs'.format(data))
        
    print('Time taken: {}s'.format(round(time.time() - start_time, 2)))


