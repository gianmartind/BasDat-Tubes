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