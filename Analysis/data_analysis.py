# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 19:37:03 2020

@author: ramak
"""



from data_preprocessing import data_preprocessing 
from collections import defaultdict
from heatmap.py import get_image_data


data_path = "data/data.csv"
output_folder = "data/images"

df = data_preprocessing(data_path,output_folder)


users = df['sysId'].unique()

print("no of users are ", len(users))

sessions = df['sessionId'].unique()

print("avg sessions per  user are" ,len(sessions)/len(users))



df1 = df.drop(columns = ['_id', '__v','gazeX','gazeY'])
urls = df1['url'].unique()

print(len(urls))
    
avg_nav_depth = defaultdict(lambda:0)


for user in users:
    user_values = df1.loc[df1['sysId'] == user]
    sessions = user_values['sessionId'].unique()
    for session in sessions:
        urls = user_values.loc[user_values['sessionId'] == session]
        unique_urls = urls['url'].unique()
        avg_nav_depth[user] +=len(unique_urls)
    
    avg_nav_depth[user]/=len(sessions)

print(avg_nav_depth)

 

##calculating avg time for each data point

df_sub = df.loc[df['sysId'] == '89648605729908210000']

avg_time = 0
for index, row in df_sub.iterrows():
    if index == 0:
        pass
    else:
        avg_time += (df_sub.iloc[index]['timestamp']-df_sub.iloc[index-1]['timestamp'])/len(df_sub.iloc[index]['gazeX'])


print(avg_time)






