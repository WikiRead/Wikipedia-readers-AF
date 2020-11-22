# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 19:37:03 2020

@author: ramak
"""



from data_preprocessing import data_preprocessing 
data_path = "data/data.csv"
output_folder = "data/images"

df = data_preprocessing(data_path,output_folder)


users = df['sysId'].unique()

print("no of users are ", len(users))

sessions = df['sessionId'].unique()

print(len(sessions))

urls = df['url'].unique()
df = df.drop(columns = ['_id', '__v','gazeX','gazeY'])
#df = df.groupby('sysId')

print(df.head(3))
    


