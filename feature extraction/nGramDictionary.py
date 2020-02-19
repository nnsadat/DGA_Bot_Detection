# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 02:07:16 2018

@author: User
"""

import textwrap
import pandas

print (textwrap.wrap("123456789", 2))
loc = 'alexa11-NgramAvgWeight.csv'
dataset = pandas.read_csv(loc, dtype='str')


pandas.set_option('display.max_columns',10)
pandas.set_option('display.max_rows',100)
pandas.set_option('display.max_colwidth',100)


for i in range(0,len(dataset)):
    s = dataset.at[i,'domain']
    b = textwrap.wrap(s, 2)
    w=0
    for j in b:
        w=w+len(j)
    bd = w/len(s)
    dataset.at[i,'bigramDict']=bd
    t = textwrap.wrap(s, 3)
    w=0
    for j in t:
        w=w+len(j)
    td = w/len(s)
    dataset.at[i,'trigramDict']=td
        
print(dataset.head(5))

dataset=dataset.astype('str')
dataset.to_csv('alexa12-NgramDictionary.csv',index=False)

loc = 'dga11-NgramAvgWeight.csv'
dataset = pandas.read_csv(loc, dtype='str')

for i in range(0,len(dataset)):
    s = dataset.at[i,'domain']
    b = textwrap.wrap(s, 2)
    w=0
    for j in b:
        w=w+len(j)
    bd = w/len(s)
    dataset.at[i,'bigramDict']=bd
    t = textwrap.wrap(s, 3)
    w=0
    for j in t:
        w=w+len(j)
    td = w/len(s)
    dataset.at[i,'trigramDict']=td
        
print(dataset.head(5))

dataset=dataset.astype('str')
dataset.to_csv('dga12-NgramDictionary.csv',index=False)