# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 19:29:10 2018

@author: User
"""
#apop
import pandas 

loc = 'alexa4-NgramWeight.csv'
dataset = pandas.read_csv(loc, dtype='str')
loc = 'alexabigramfrequency.csv'
DSbigram = pandas.read_csv(loc, dtype='str')
loc = 'alexatrigramfrequency.csv'
DStrigram = pandas.read_csv(loc, dtype='str')
loc = 'allpossiblebigrams.csv'
TSbigram = pandas.read_csv(loc, dtype='str')
loc = 'allpossibletrigrams.csv'
TStrigram = pandas.read_csv(loc, dtype='str')

pandas.set_option('display.max_columns',10)
pandas.set_option('display.max_rows',100)
pandas.set_option('display.max_colwidth',100)

for i in range(0,len(dataset)):

    bc = float(dataset.at[i,'bigramCount'])
    blen = dataset.at[i,'bigramLen']
    if (int(blen)==0):
        bpop=0
    else:      
        bpop = int(bc)/int(blen)
    dataset.at[i,'bigramPop']=bpop
    
    tc = float(dataset.at[i,'trigramCount'])
    tlen = dataset.at[i,'trigramLen']
    if (int(tlen)==0):
        tpop=0
    else:
        tpop = int(tc)/int(tlen)
    dataset.at[i,'trigramPop']=tpop

print(dataset.head(5))

dataset=dataset.astype('str')
dataset.to_csv('alexa5-NgramPop.csv', index=False)

loc = 'dga4-NgramWeight.csv'
dataset = pandas.read_csv(loc, dtype='str')
for i in range(0,len(dataset)):

    bc = float(dataset.at[i,'bigramCount'])
    blen = dataset.at[i,'bigramLen']
    if (int(blen)==0):
        bpop=0
    else:      
        bpop = int(bc)/int(blen)
    dataset.at[i,'bigramPop']=bpop
    
    tc = float(dataset.at[i,'trigramCount'])
    tlen = dataset.at[i,'trigramLen']
    if (int(tlen)==0):
        tpop=0
    else:
        tpop = int(tc)/int(tlen)
    dataset.at[i,'trigramPop']=tpop

print(dataset.head(5))

dataset=dataset.astype('str')
dataset.to_csv('dga5-NgramPop.csv', index=False)