# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 19:37:03 2020

@author: ramak
"""



from data_preprocessing import data_preprocessing 
from collections import defaultdict
from heatmap import get_image_data
import json


data_path = "data/data.csv"
output_folder = "data/images"

df = data_preprocessing(data_path,output_folder)


users = df['sysId'].unique()

print("no of users are ", len(users))

sessions = df['sessionId'].unique()

print("avg sessions per  user are" ,len(sessions)/len(users))



df1 = df.drop(columns = ['_id', '__v','gazeY'])
urls = df1['url'].unique()

print(len(urls))
    
##calculating avg time for each data point

df_sub = df.loc[df['sysId'] == '89648605729908210000']

avg_time = 0
for index, row in df_sub.iterrows():
    if index == 0:
        pass
    else:
        avg_time += (df_sub.iloc[index]['timestamp']-df_sub.iloc[index-1]['timestamp'])/len(json.loads(df_sub.iloc[index]['gazeX']))


print(avg_time)

freqs = get_image_data(df)

times = []

for index, row in df.iterrows():
    time = len(df.iloc[index]['gazeX'])*avg_time/1000
    times.append(time)

avg_nav_depth = defaultdict(lambda:0)
time_per_user = defaultdict(lambda:0)

for user in users:
    user_values = df1.loc[df1['sysId'] == user]
    sessions = user_values['sessionId'].unique()
    for session in sessions:
        urls = user_values.loc[user_values['sessionId'] == session]
        unique_urls = urls['url'].unique()
        gaze_data = urls['gazeX']
        avg_nav_depth[user] +=len(unique_urls)
        time_per_user[user] += sum([len(json.loads(x)) for x in gaze_data])
    
    avg_nav_depth[user]/=len(sessions)
    time_per_user[user]/=len(sessions)

print(avg_nav_depth)
print(time_per_user)
    
time_with_pictures = 0
no_data_with_pictures = 0
time_without_pictures = 0
no_data_without_pictures = 0
for index,freq in enumerate(freqs):
    if freq ==0:
        no_data_without_pictures+=1
        time_without_pictures+=times[index]
    else:
        no_data_with_pictures+=1
        time_with_pictures+=times[index]


    