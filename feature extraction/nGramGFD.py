# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 14:30:57 2018

@author: User
"""

import pandas
import numpy    
from sklearn.feature_extraction.text import CountVectorizer 

loc = 'alexa2-NgramCount.csv'
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

bigramVectorizer = CountVectorizer(ngram_range=(2,2),analyzer='char')
trigramVectorizer = CountVectorizer(ngram_range=(3,3),analyzer='char')
bigramAnalyzer = bigramVectorizer.build_analyzer()
trigramAnalyzer = trigramVectorizer.build_analyzer()
    
for i in range(0,len(dataset)):
    domain=dataset['domain'].loc[i]
    
    str=bigramAnalyzer(domain)
    gfd=0
    for t in range(0,len(str)):
        f = DSbigram.loc[DSbigram['bigram']==str[t],'frequency']
        index = TSbigram.loc[TSbigram['TSbigram']==str[t],'Rank'] 
        if len(f)==0:
            f=0
        else:
            f=f.iloc[0]
        if len(index)==0:
            index=0
        else:
            index=int(index.iloc[0])+1
        result = int(f) * index
        gfd=gfd+result
    g=int(gfd)
    dataset.at[i,'bigramGFD']=g
    
    str=trigramAnalyzer(domain)
    gfd=0
    for t in range(0,len(str)):
        f = DStrigram.loc[DStrigram['trigram']==str[t],'frequency']
        index = TStrigram.loc[TStrigram['TStrigram']==str[t],'Rank'] 
        if len(f)==0:
            f=0
        else:
            f=f.iloc[0]
        if len(index)==0:
            index=0
        else:
            index=int(index.iloc[0])+1
        result = int(f) * index
        gfd=gfd+result
    g=int(gfd)
    dataset.at[i,'trigramGFD']=g
    
print(dataset.head(5))

dataset=dataset.astype('str')
dataset.to_csv('alexa3-NgramGFD.csv', index=False)

loc = 'dga2-NgramCount.csv'
dataset = pandas.read_csv(loc, dtype='str')

for i in range(0,len(dataset)):
    domain=dataset['domain'].loc[i]
    
    str=bigramAnalyzer(domain)
    gfd=0
    for t in range(0,len(str)):
        f = DSbigram.loc[DSbigram['bigram']==str[t],'frequency']
        index = TSbigram.loc[TSbigram['TSbigram']==str[t],'Rank'] 
        if len(f)==0:
            f=0
        else:
            f=f.iloc[0]
        if len(index)==0:
            index=0
        else:
            index=int(index.iloc[0])+1
        result = int(f) * index
        gfd=gfd+result
    g=int(gfd)
    dataset.at[i,'bigramGFD']=g
    
    str=trigramAnalyzer(domain)
    gfd=0
    for t in range(0,len(str)):
        f = DStrigram.loc[DStrigram['trigram']==str[t],'frequency']
        index = TStrigram.loc[TStrigram['TStrigram']==str[t],'Rank'] 
        if len(f)==0:
            f=0
        else:
            f=f.iloc[0]
        if len(index)==0:
            index=0
        else:
            index=int(index.iloc[0])+1
        result = int(f) * index
        gfd=gfd+result
    g=int(gfd)
    dataset.at[i,'trigramGFD']=g
    
print(dataset.head(5))

dataset=dataset.astype('str')
dataset.to_csv('dga3-NgramGFD.csv', index=False)