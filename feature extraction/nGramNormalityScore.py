# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 18:58:15 2018

@author: User
"""
#normality score
import pandas
import collections 
from sklearn.feature_extraction.text import CountVectorizer 

loc = 'alexa7-NgramEntropy2.csv'
dataset = pandas.read_csv(loc)
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
    c=collections.Counter(str)
    it = set()
    for x in str:
        it.add(x)
    ns=0.0
    for t in it:
        count=c[t]
        f = DSbigram.loc[DSbigram['bigram']==t,'frequency']
        if len(f)==0:
            f=0
        else:
            f=f.iloc[0]
        result =  count*int(f)
        ns = ns+result
    ns = ns/(len(dataset['domain'].loc[i]))
    dataset.at[i,'bigramNS']=ns
        
    str=trigramAnalyzer(domain)
    c=collections.Counter(str)
    it = set()
    for x in str:
        it.add(x)
    ns=0.0
    for t in it:
        count=c[t]
        f = DStrigram.loc[DStrigram['trigram']==t,'frequency']
        if len(f)==0:
            f=0
        else:
            f=f.iloc[0]
        result =  count*int(f)
        ns = ns+result
    ns = ns/(len(dataset['domain'].loc[i]))
    dataset.at[i,'trigramNS']=ns
        
        
print(dataset.head(5))

dataset=dataset.astype('str')
dataset.to_csv('alexa8-NgramNormalityScore.csv', index=False)

loc = 'dga7-NgramEntropy2.csv'
dataset = pandas.read_csv(loc)

for i in range(0,len(dataset)):
    
    domain=dataset['domain'].loc[i]
    
    str=bigramAnalyzer(domain)
    c=collections.Counter(str)
    it = set()
    for x in str:
        it.add(x)
    ns=0.0
    for t in it:
        count=c[t]
        f = DSbigram.loc[DSbigram['bigram']==t,'frequency']
        if len(f)==0:
            f=0
        else:
            f=f.iloc[0]
        result =  count*int(f)
        ns = ns+result
    ns = ns/(len(dataset['domain'].loc[i]))
    dataset.at[i,'bigramNS']=ns
        
    str=trigramAnalyzer(domain)
    c=collections.Counter(str)
    it = set()
    for x in str:
        it.add(x)
    ns=0.0
    for t in it:
        count=c[t]
        f = DStrigram.loc[DStrigram['trigram']==t,'frequency']
        if len(f)==0:
            f=0
        else:
            f=f.iloc[0]
        result =  count*int(f)
        ns = ns+result
    ns = ns/(len(dataset['domain'].loc[i]))
    dataset.at[i,'trigramNS']=ns
        
        
print(dataset.head(5))

dataset=dataset.astype('str')
dataset.to_csv('dga8-NgramNormalityScore.csv', index=False)