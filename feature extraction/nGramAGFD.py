# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 19:29:10 2018

@author: User
"""
#agfd
import pandas

loc = 'alexa9-NgramEntropy1.csv'
dataset = pandas.read_csv(loc, dtype='str')

pandas.set_option('display.max_columns',10)
pandas.set_option('display.max_rows',100)
pandas.set_option('display.max_colwidth',100)

for i in range(0,len(dataset)):
    bgfd = float(dataset.at[i,'bigramGFD'])
    blen = dataset.at[i,'bigramLen']
    if (int(blen)==0):
        bagfd=0
    else:
        bagfd = int(bgfd)/int(blen)
    dataset.at[i,'bigramAGFD']=bagfd
    
    tgfd = float(dataset.at[i,'trigramGFD'])
    tlen = dataset.at[i,'trigramLen']
    if (int(tlen)==0):
        tagfd=0
    else:
        tagfd = int(tgfd)/int(tlen)
    dataset.at[i,'trigramAGFD']=tagfd

print(dataset.head(5))

dataset=dataset.astype('str')
dataset.to_csv('alexa10-NgramAGFD.csv', index=False)

loc = 'dga9-NgramEntropy1.csv'
dataset = pandas.read_csv(loc, dtype='str')
for i in range(0,len(dataset)):
    bgfd = float(dataset.at[i,'bigramGFD'])
    blen = dataset.at[i,'bigramLen']
    if (int(blen)==0):
        bagfd=0
    else:
        bagfd = int(bgfd)/int(blen)
    dataset.at[i,'bigramAGFD']=bagfd
    
    tgfd = float(dataset.at[i,'trigramGFD'])
    tlen = dataset.at[i,'trigramLen']
    if (int(tlen)==0):
        tagfd=0
    else:
        tagfd = int(tgfd)/int(tlen)
    dataset.at[i,'trigramAGFD']=tagfd

print(dataset.head(5))

dataset=dataset.astype('str')
dataset.to_csv('dga10-NgramAGFD.csv', index=False)