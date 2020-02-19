# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 22:05:11 2018

@author: User
"""
#count
import pandas

from sklearn.feature_extraction.text import CountVectorizer 

loc = 'alexa1-NgramLength.csv'
dataset = pandas.read_csv(loc, dtype='str')
loc = 'alexabigramfrequency.csv'
DSbigram = pandas.read_csv(loc, dtype='str')
loc = 'alexatrigramfrequency.csv'
DStrigram = pandas.read_csv(loc, dtype='str')

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
        c=0
        for t in range(0,len(str)):
            if str[t] in DSbigram['bigram'].values:
                c=c+1
        count=int(c)
        dataset.at[i,'bigramCount']=count
        
        str=trigramAnalyzer(domain)
        c=0
        for t in range(0,len(str)):
            if str[t] in DStrigram['trigram'].values:
                c=c+1
        count=int(c)
        dataset.at[i,'trigramCount']=count

print(dataset.head(5))
dataset['domain']=dataset['domain'].astype('str')
dataset.to_csv('alexa2-NgramCount.csv', index=False)

loc = 'dga1-NgramLength.csv'
dataset = pandas.read_csv(loc, dtype='str')

for i in range(0,len(dataset)):
        domain=dataset['domain'].loc[i]
        
        str=bigramAnalyzer(domain)
        c=0
        for t in range(0,len(str)):
            if str[t] in DSbigram['bigram'].values:
                c=c+1
        count=int(c)
        dataset.at[i,'bigramCount']=count
        
        str=trigramAnalyzer(domain)
        c=0
        for t in range(0,len(str)):
            if str[t] in DStrigram['trigram'].values:
                c=c+1
        count=int(c)
        dataset.at[i,'trigramCount']=count

print(dataset.head(5))
dataset['domain']=dataset['domain'].astype('str')
dataset.to_csv('dga2-NgramCount.csv', index=False)