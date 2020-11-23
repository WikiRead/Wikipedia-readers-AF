# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 19:37:03 2020

@author: ramak
"""



from data_preprocessing import data_preprocessing 
from collections import defaultdict


data_path = "data/data.csv"
output_folder = "data/images"

df = data_preprocessing(data_path,output_folder)


users = df['sysId'].unique()

print("no of users are ", len(users))

sessions = df['sessionId'].unique()

print("avg sessions per  user are" ,len(sessions)/len(users))

urls = df['url'].unique()

df1 = df.drop(columns = ['_id', '__v','gazeX','gazeY'])
    
avg_nav_depth = defaultdict(lambda:0)


for user in users:
    user_values = df1.loc[df1['sysId'] == user]
    sessions = user_values['sessionId'].unique()
    #print("no of sessions",len(sessions))
    for session in sessions:
        unique_urls = user_values.loc[user_values['sessionId'] == session]
        #print(unique_urls)
        avg_nav_depth[user] +=len(unique_urls)
    
    avg_nav_depth[user]/=len(sessions)

print(avg_nav_depth)

urls = df1.loc[df1['sysId'] == '80677021885377460000']['url']

