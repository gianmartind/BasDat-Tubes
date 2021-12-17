# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 22:17:26 2021

@author: gianm
"""

#%%
import dataset
import pandas as pd

#%%
github_data = dataset.download_github_data([3, 4])

#%% owid-covid-data
df_owid = github_data['owid-covid-data.csv']

#pilih hanya kolom yang digunakan
df_owid = df_owid[['continent', 'location', 'date', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths']]

#ubah nan menjadi 0
df_owid.fillna(0, inplace=True)
