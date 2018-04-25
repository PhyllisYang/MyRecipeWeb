#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 18:03:42 2018

@author: fanyang
"""

import csv
import pandas as pd



file = '/Users/fanyang/python/finalproject/recipe_data 2.csv'

f=pd.read_csv(file)
X = pd.DataFrame(f)
X.drop(X[X['ingredients']== 'None'].index,inplace=True)
X.to_csv("/Users/fanyang/python/finalproject/newrecipe_data.csv",index=False,sep=',')
    
