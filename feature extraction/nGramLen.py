# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 18:12:32 2018

@author: User
"""
from sklearn.feature_extraction.text import CountVectorizer 
import pandas


loc = 'alexa.csv'
dataset = pandas.read_csv(loc, dtype='str')
pandas.set_option('display.max_columns',10)
pandas.set_option('display.max_rows',100)
pandas.set_option('display.max_colwidth',100)

dataset['bigramLen']=0
dataset['trigramLen']=0
#dataset=dataset['domain'].values.astype('U')
for i in range(0,len(dataset)):    
    vectorizer = CountVectorizer(ngram_range=(2,2),analyzer='char')
    a = vectorizer.build_analyzer()
    #print(dataset.at[i,'domain'])
    bigram=a(dataset.at[i,'domain'])
    dataset.at[i,'bigramLen']=len(bigram)
    
    vectorizer = CountVectorizer(ngram_range=(3,3),analyzer='char')
    a = vectorizer.build_analyzer()
    trigram=a(dataset['domain'].loc[i])
    dataset.at[i,'trigramLen']=len(trigram)
    
#dataset=dataset[['domain','malware','bigramLen','trigramLen']].copy()
print(dataset.head(5))
dataset=dataset.astype('str')
dataset.to_csv('alexa1-NgramLength.csv', index=False)

loc = 'dga.csv'
dataset = pandas.read_csv(loc, dtype='str')

dataset['bigramLen']=0
dataset['trigramLen']=0
#dataset=dataset['domain'].values.astype('U')
for i in range(0,len(dataset)):    
    vectorizer = CountVectorizer(ngram_range=(2,2),analyzer='char')
    a = vectorizer.build_analyzer()
    #print(dataset.at[i,'domain'])
    bigram=a(dataset.at[i,'domain'])
    dataset.at[i,'bigramLen']=len(bigram)
    
    vectorizer = CountVectorizer(ngram_range=(3,3),analyzer='char')
    a = vectorizer.build_analyzer()
    trigram=a(dataset['domain'].loc[i])
    dataset.at[i,'trigramLen']=len(trigram)
    
#dataset=dataset[['domain','malware','bigramLen','trigramLen']].copy()
print(dataset.head(5))
dataset=dataset.astype('str')
dataset.to_csv('dga1-NgramLength.csv', index=False)