# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 00:54:00 2018

@author: User
"""
#Removing least occuring DGAs and TLDs of both alexa and dga dataset
import pandas

pandas.set_option('display.max_columns',10)
pandas.set_option('display.max_rows',100)
pandas.set_option('display.max_colwidth',100)

loc = 'dga16-AvgCharFreq.csv'
df1 = pandas.read_csv(loc, index_col=False)

loc = 'alexa16-AvgCharFreq.csv'
df2 = pandas.read_csv(loc, index_col=False)

dataset=df1.append(df2,ignore_index=True)
dataset=dataset.sample(frac=1).reset_index(drop=True)
print(dataset.head(20))
dataset['domain']=dataset['domain'].astype('str')
dataset.to_csv('combinedDataset.csv',index=False)
