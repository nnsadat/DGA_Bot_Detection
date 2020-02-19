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

loc = 'dga-ORIGINAL.csv'
df1 = pandas.read_csv(loc)

print(df1.head(5))
print(df1['malware'].value_counts())
df1=df1[df1.malware!='g01']
df1=df1[df1.malware!='madmax']
df1=df1[df1.malware!='dromedan']
df1=df1[df1.malware!='mirai']
df1=df1[df1.malware!='gozi']
df1=df1[df1.malware!='pandabanker']
df1=df1[df1.malware!='sisron']
df1=df1[df1.malware!='unknowndropper']
df1=df1[df1.malware!='Domain used by cryptowall - static observed list']
df1=df1[df1.malware!='bedep']
df1=df1[df1.malware!='unknownjs']
df1=df1.join(df1['domain'].str.split('.',expand=True).add_prefix('domain'))
df1 = df1[['domain0', 'malware']].copy()
df1.columns = ['domain','class']
print(df1.head(5))
print(df1['class'].value_counts())
df1['class']= 'dga'
print(df1.head(5))
df1.to_csv('dga.csv')
#print(len(dataset.index))

loc = 'alexa-ORIGINAL.csv'
df2 = pandas.read_csv(loc)

df2=df2.join(df2['Website'].str.split('.',expand=True).add_prefix('Website'))
df2 = df2[['Website0']].copy()
df2.columns = ['domain']
df2=df2.drop_duplicates(subset=None,keep='first',inplace=False)
df2['class']= 'legit'
print(df2.head(5))
df2 = df2[['domain','class']].copy()
df2['domain']=df2['domain'].astype('str')
df2.to_csv('alexa.csv')
#print(len(dataset.index))

dataset=df1.append(df2,ignore_index=True)
dataset=dataset.sample(frac=1).reset_index(drop=True)
print(dataset.head(20))
dataset['domain']=dataset['domain'].astype('str')
dataset.to_csv('dataset.csv')
