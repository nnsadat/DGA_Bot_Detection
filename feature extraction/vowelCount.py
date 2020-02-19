# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 18:58:15 2018

@author: User
"""
#vowelcount
import pandas

loc = 'alexa13-DomLength.csv'
dataset = pandas.read_csv(loc, dtype='str')


pandas.set_option('display.max_columns',10)
pandas.set_option('display.max_rows',100)
pandas.set_option('display.max_colwidth',100)

for i in range(0,len(dataset)):
    s=dataset.at[i,'domain']
    counter = len([c for c in s if c in 'aeiou'])
    dataset.at[i,'vowelCount']=counter
        
print(dataset.head(5))

dataset=dataset.astype('str')
dataset.to_csv('alexa14-VowelCount.csv',index=False)

loc = 'dga13-DomLength.csv'
dataset = pandas.read_csv(loc, dtype='str')

for i in range(0,len(dataset)):
    s=dataset.at[i,'domain']
    counter = len([c for c in s if c in 'aeiou'])
    dataset.at[i,'vowelCount']=counter
        
print(dataset.head(5))

dataset=dataset.astype('str')
dataset.to_csv('dga14-VowelCount.csv',index=False)

