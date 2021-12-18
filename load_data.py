# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 22:17:26 2021

@author: gianm
"""

#%% import library
import dataset
import pandas as pd

#%% download data
github_data = dataset.download_github_data([0, 3])

#%% owid-covid-data
df_owid = github_data['owid-covid-data.csv']

#pilih hanya kolom yang digunakan
df_owid = df_owid[['continent', 'location', 'date', 'new_cases', 'new_deaths']]

#ubah nilai nan menjadi 0
df_owid.fillna(0, inplace=True)

#hapus baris dengan continent == 0
df_owid = df_owid[df_owid['continent'] != 0]

#gunakan hanya tahun 2021
df_owid = df_owid[df_owid['date'].str.startswith('2021')]

#%% vaccine-by-manufacturers
df_vacc = github_data['vaccinations.csv']

#pilih hanya kolom yang digunakan
df_vacc = df_vacc[['location', 'date', 'daily_vaccinations']]

#ubah nilai nan menjadi 0
df_vacc.fillna(0, inplace=True)

#gunakan hanya tahun 2021
df_vacc = df_vacc[df_owid['date'].str.startswith('2021')]

#%% load to hdfs
cleaned_datasets = dict()
cleaned_datasets['owid-covid-data.csv'] = df_owid
cleaned_datasets['vaccinations.csv'] = df_vacc

dataset.load_to_hdfs(cleaned_datasets)

