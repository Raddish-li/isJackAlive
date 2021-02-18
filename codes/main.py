# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 19:36:44 2020

@author: Siddharth
"""


import os
import numpy as np
import pandas as pd


# Reading in datasets
repo_path = r'C:\Users\Siddharth\Desktop\Py projects\isJackAlive'
code_path = os.path.join(repo_path, 'codes')
dat_path = os.path.join(repo_path, 'data')

train_data = pd.read_csv(os.path.join(dat_path, 'train.csv'))
