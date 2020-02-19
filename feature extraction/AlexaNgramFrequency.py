# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 22:54:32 2018

@author: User
"""

import pandas
from sklearn.feature_extraction.text import CountVectorizer

loc = 'alexa.csv'
dataset = pandas.read_csv(loc)
pandas.set_option('display.max_columns',10)
pandas.set_option('display.max_rows',100)
pandas.set_option('display.max_colwidth',100)

char_vectorizer = CountVectorizer(ngram_range=(2,2), analyzer='char')
sparse_matrix = char_vectorizer.fit_transform(dataset['domain'].values.astype('U'))
frequencies = sum(sparse_matrix).toarray()[0]
data=pandas.DataFrame(frequencies, index=char_vectorizer.get_feature_names(),columns=['frequency'])
data=data.sort_values(by='frequency',ascending=0)
data.index.names = ['bigram']
data=data.astype('str')
data.to_csv('alexabigramfrequency.csv')
loc = 'alexabigramfrequency.csv'
alexaBigram = pandas.read_csv(loc, dtype='str')
print(alexaBigram.head(5))

char_vectorizer = CountVectorizer(ngram_range=(3,3), analyzer='char')
sparse_matrix = char_vectorizer.fit_transform(dataset['domain'].values.astype('U'))
frequencies = sum(sparse_matrix).toarray()[0]
data=pandas.DataFrame(frequencies, index=char_vectorizer.get_feature_names(),columns=['frequency'])
data=data.sort_values(by='frequency',ascending=0)
data.index.names = ['trigram']
data=data.astype('str')
data.to_csv('alexatrigramfrequency.csv')
loc = 'alexatrigramfrequency.csv'
alexaTrigram = pandas.read_csv(loc, dtype='str')
print(alexaTrigram.head(5))

