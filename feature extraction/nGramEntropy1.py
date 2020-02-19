"""
Created on Sun Jul 22 18:58:15 2018

@author: User
"""
#entropy
import pandas
import math  
from sklearn.feature_extraction.text import CountVectorizer 

loc = 'alexa8-NgramNormalityScore.csv'
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

    l=len(DSbigram)
    entropy=0.0
    for t in range(0,len(str)):
        vt = DSbigram[DSbigram.bigram==str[t]].index 
        if len(vt)==0:
            vt=int(0)
            result = 0
        else:
            vt=int(vt[0])+1
            x =  (int(vt)/l)
            result = x*math.log(x)
        entropy = entropy+result
    entropy = entropy * (-1)
    dataset.at[i,'bigramEntropy1']=entropy
        
    l=len(DStrigram)
    
    str=trigramAnalyzer(domain)
    entropy=0.0
    for t in range(0,len(str)):
        vt = DStrigram[DStrigram.trigram==str[t]].index 
        if len(vt)==0:
            vt=int(0)
            result = 0
        else:
            vt=int(vt[0])+1
            x =  (int(vt)/l)
            result = x*math.log(x)
        entropy = entropy+result
    entropy = entropy * (-1)
    dataset.at[i,'trigramEntropy1']=entropy
        
print(dataset.head(5))

dataset=dataset.astype('str')
dataset.to_csv('alexa9-NgramEntropy1.csv', index=False)


loc = 'dga8-NgramNormalityScore.csv'
dataset = pandas.read_csv(loc, dtype='str')
for i in range(0,len(dataset)):
    
    domain=dataset['domain'].loc[i]
    
    str=bigramAnalyzer(domain)

    l=len(DSbigram)
    entropy=0.0
    for t in range(0,len(str)):
        vt = DSbigram[DSbigram.bigram==str[t]].index 
        if len(vt)==0:
            vt=int(0)
            result = 0
        else:
            vt=int(vt[0])+1
            x =  (int(vt)/l)
            result = x*math.log(x)
        entropy = entropy+result
    entropy = entropy * (-1)
    dataset.at[i,'bigramEntropy1']=entropy
        
    l=len(DStrigram)
    
    str=trigramAnalyzer(domain)
    entropy=0.0
    for t in range(0,len(str)):
        vt = DStrigram[DStrigram.trigram==str[t]].index 
        if len(vt)==0:
            vt=int(0)
            result = 0
        else:
            vt=int(vt[0])+1
            x =  (int(vt)/l)
            result = x*math.log(x)
        entropy = entropy+result
    entropy = entropy * (-1)
    dataset.at[i,'trigramEntropy1']=entropy
        
print(dataset.head(5))

dataset=dataset.astype('str')
dataset.to_csv('dga9-NgramEntropy1.csv', index=False)
