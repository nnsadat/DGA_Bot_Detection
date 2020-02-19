# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 18:58:15 2018

@author: User
"""
#entropyfrom2
import pandas
import collections 
import math  
from sklearn.feature_extraction.text import CountVectorizer 

loc = 'alexa6-NgramAvgFreq.csv'
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
    c=collections.Counter(str)
    it = set()
    for x in str:
        it.add(x)
    entropy=0.0
    for t in it:
        count=c[t]
        z =  count/len(str)
        result = z*math.log(z)
        entropy = entropy+result
    entropy = entropy * (-1)
    dataset.at[i,'bigramEntropy']=entropy
    
    str=trigramAnalyzer(domain)
    c=collections.Counter(str)
    it = set()
    for x in str:
        it.add(x)
    entropy=0.0
    for t in it:
        count=c[t]
        z =  count/len(str)
        result = z*math.log(z)
        entropy = entropy+result
    entropy = entropy * (-1)
    dataset.at[i,'trigramEntropy']=entropy
        
        
print(dataset.head(5))

dataset=dataset.astype('str')
dataset.to_csv('alexa7-NgramEntropy2.csv', index=False)

loc = 'dga6-NgramAvgFreq.csv'
dataset = pandas.read_csv(loc, dtype='str')
for i in range(0,len(dataset)):
    
    domain=dataset['domain'].loc[i]
    
    str=bigramAnalyzer(domain)
    c=collections.Counter(str)
    it = set()
    for x in str:
        it.add(x)
    entropy=0.0
    for t in it:
        count=c[t]
        z =  count/len(str)
        result = z*math.log(z)
        entropy = entropy+result
    entropy = entropy * (-1)
    dataset.at[i,'bigramEntropy']=entropy
    
    str=trigramAnalyzer(domain)
    c=collections.Counter(str)
    it = set()
    for x in str:
        it.add(x)
    entropy=0.0
    for t in it:
        count=c[t]
        z =  count/len(str)
        result = z*math.log(z)
        entropy = entropy+result
    entropy = entropy * (-1)
    dataset.at[i,'trigramEntropy']=entropy
        
        
print(dataset.head(5))

dataset=dataset.astype('str')
dataset.to_csv('dga7-NgramEntropy2.csv', index=False)