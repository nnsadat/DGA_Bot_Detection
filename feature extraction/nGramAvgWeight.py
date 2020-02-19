# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 19:29:10 2018

@author: User
"""
#aweight
import pandas 

loc = 'alexa10-NgramAGFD.csv'
dataset = pandas.read_csv(loc, dtype='str')

pandas.set_option('display.max_columns',10)
pandas.set_option('display.max_rows',100)
pandas.set_option('display.max_colwidth',100)


for i in range(0,len(dataset)):
    bwt = float(dataset.at[i,'bigramWt'])
    blen = dataset.at[i,'bigramLen']
    if (int(blen)==0):
        bawt=0
    else:
        bawt = int(bwt)/int(blen)
    dataset.at[i,'bigramAW']=bawt
    
    twt = float(dataset.at[i,'trigramWt'])
    tlen = dataset.at[i,'trigramLen']
    if (int(tlen)==0):
        tawt=0
    else:
         tawt = int(twt)/int(tlen)
    dataset.at[i,'trigramAW']=tawt

print(dataset.head(5))

dataset=dataset.astype('str')
dataset.to_csv('alexa11-NgramAvgWeight.csv', index=False)

loc = 'dga10-NgramAGFD.csv'
dataset = pandas.read_csv(loc, dtype='str')

for i in range(0,len(dataset)):
    bwt = float(dataset.at[i,'bigramWt'])
    blen = dataset.at[i,'bigramLen']
    if (int(blen)==0):
        bawt=0
    else:
        bawt = int(bwt)/int(blen)
    dataset.at[i,'bigramAW']=bawt
    
    twt = float(dataset.at[i,'trigramWt'])
    tlen = dataset.at[i,'trigramLen']
    if (int(tlen)==0):
        tawt=0
    else:
         tawt = int(twt)/int(tlen)
    dataset.at[i,'trigramAW']=tawt

print(dataset.head(5))

dataset=dataset.astype('str')
dataset.to_csv('dga11-NgramAvgWeight.csv', index=False)