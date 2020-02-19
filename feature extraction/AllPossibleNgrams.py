# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 01:45:04 2018

@author: User
"""
import pandas

x=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','.','-']
TSbigrams=[]


for i in range(0,38):
    for j in range(0,38):
        y=[]
        y.append(x[i])
        y.append(x[j])
        z=''.join(y)
        TSbigrams.append(z)
        
print(len(TSbigrams))
df1=pandas.DataFrame(TSbigrams,columns=['TSbigram']) 
print(df1.head(5))
df1.index.names = ['Rank']
df1=df1.astype('str')
df1.to_csv('allpossiblebigrams.csv')
loc='allpossiblebigrams.csv'
df2=pandas.read_csv(loc, dtype='str')
print(df2.head(5))

TStrigrams=[]

for i in range(0,38):
    for j in range(0,38):
        for k in range(0,38):
            y=[]
            y.append(x[i])
            y.append(x[j])
            y.append(x[k])
            z=''.join(y)
            TStrigrams.append(z)
    

print(len(TStrigrams))
df1=pandas.DataFrame(TStrigrams,columns=['TStrigram']) 
print(df1.head(5))
df1.index.names = ['Rank']
df1=df1.astype('str')
df1.to_csv('allpossibletrigrams.csv')
loc='allpossibletrigrams.csv'
df2=pandas.read_csv(loc, dtype='str')
print(df2.head(5))
