# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 19:39:24 2020

@author: ramak
"""

from urllib import request
import pandas as pd

data_path = "data/data.csv"
output_folder = "data/images"
def data_preprocessing(data_path, output_folder):
    
    df = pd.read_csv(data_path)

    images = df['image']

    for index, row in df.iterrows():
        data_uri = row['image']
        with request.urlopen(data_uri) as response:
            data = response.read()
        
        with open(output_folder+"/image"+str(index)+".png", "wb+") as f:
            f.write(data)
    
    return df 