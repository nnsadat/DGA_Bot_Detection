# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 20:30:45 2018

@author: User
"""

import pandas

# load data
loc = 'alexa12-NgramDictionary.csv'
dataset = pandas.read_csv(loc)
for i in range(0,len(dataset)):
    s=dataset.at[i,'domain']
    dataset.at[i,'domainLen'] = len(s)
print(dataset.head(5))
dataset=dataset.astype('str')
dataset.to_csv('alexa13-DomLength.csv',index=False)

loc = 'dga12-NgramDictionary.csv'
dataset = pandas.read_csv(loc)
for i in range(0,len(dataset)):
    s=dataset.at[i,'domain']
    dataset.at[i,'domainLen'] = len(s)
print(dataset.head(5))
dataset=dataset.astype('str')
dataset.to_csv('dga13-DomLength.csv',index=False)