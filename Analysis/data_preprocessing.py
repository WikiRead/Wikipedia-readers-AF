# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 19:39:24 2020

@author: ramak
"""

from urllib import request
import pandas as pd

df = pd.read_csv("data/data.csv")

images = df['image']

for index, row in df.iterrows():
    data_uri = row['image']
    with request.urlopen(data_uri) as response:
        data = response.read()
        
    with open("data/images/image"+str(index)+".png", "wb+") as f:
        f.write(data)