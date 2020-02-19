# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 18:58:15 2018

@author: User
"""

import pandas
from sklearn.feature_extraction.text import CountVectorizer 

loc = 'alexa3-NgramGFD.csv'
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
    weight=0
    c = float(dataset.at[i,'bigramCount'])
    for t in range(0,len(str)):
        f = DSbigram.loc[DSbigram['bigram']==str[t],'frequency']
        vt = DSbigram[DSbigram.bigram==str[t]].index
        
        if len(f)==0:
            f=0
        else:
            f=f.iloc[0]
        if len(vt)==0:
            vt=int(0)
        else:
            vt=int(vt[0])+1
        result = int(f) * vt
        weight = weight+result
    if (int(c)!=0):
        r = int(weight/int(c))
    else:
        r=0
    dataset.at[i,'bigramWt']=r
    
    str=trigramAnalyzer(domain)
    weight=0
    c = float(dataset.at[i,'trigramCount'])
    for t in range(0,len(str)):
        f = DStrigram.loc[DStrigram['trigram']==str[t],'frequency']
        vt = DStrigram[DStrigram.trigram==str[t]].index
        
        if len(f)==0:
            f=0
        else:
            f=f.iloc[0]
        if len(vt)==0:
            vt=int(0)
        else:
            vt=int(vt[0])+1
        result = int(f) * vt
        weight = weight+result
    if (int(c)!=0):
        r = int(weight/int(c))
    else:
        r=0
    dataset.at[i,'trigramWt']=r
        
        
print(dataset.head(5))

dataset=dataset.astype('str')
dataset.to_csv('alexa4-NgramWeight.csv', index=False)

loc = 'dga3-NgramGFD.csv'
dataset = pandas.read_csv(loc, dtype='str')

for i in range(0,len(dataset)):
    domain=dataset['domain'].loc[i]
    
    str=bigramAnalyzer(domain)
    weight=0
    c = float(dataset.at[i,'bigramCount'])
    for t in range(0,len(str)):
        f = DSbigram.loc[DSbigram['bigram']==str[t],'frequency']
        vt = DSbigram[DSbigram.bigram==str[t]].index
        
        if len(f)==0:
            f=0
        else:
            f=f.iloc[0]
        if len(vt)==0:
            vt=int(0)
        else:
            vt=int(vt[0])+1
        result = int(f) * vt
        weight = weight+result
    if (int(c)!=0):
        r = int(weight/int(c))
    else:
        r=0
    dataset.at[i,'bigramWt']=r
    
    str=trigramAnalyzer(domain)
    weight=0
    c = float(dataset.at[i,'trigramCount'])
    for t in range(0,len(str)):
        f = DStrigram.loc[DStrigram['trigram']==str[t],'frequency']
        vt = DStrigram[DStrigram.trigram==str[t]].index
        
        if len(f)==0:
            f=0
        else:
            f=f.iloc[0]
        if len(vt)==0:
            vt=int(0)
        else:
            vt=int(vt[0])+1
        result = int(f) * vt
        weight = weight+result
    if (int(c)!=0):
        r = int(weight/int(c))
    else:
        r=0
    dataset.at[i,'trigramWt']=r
        
        
print(dataset.head(5))

dataset=dataset.astype('str')
dataset.to_csv('dga4-NgramWeight.csv', index=False)