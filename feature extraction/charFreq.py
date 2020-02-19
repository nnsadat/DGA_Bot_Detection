# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 17:26:34 2018

@author: User
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 16:32:51 2018

@author: User
"""

import pandas

loc = 'alexa15-NgramAvgVowel.csv'
dataset = pandas.read_csv(loc)
pandas.set_option('display.max_columns',40)
dataset.head(5)

for i in range(0,len(dataset)):
    s=dataset.at[i,'domain']
    
    dataset.at[i,'a']=float(s.count('a'))/len(s)
    dataset.at[i,'b']=float(s.count('b'))/len(s)
    dataset.at[i,'c']=float(s.count('c'))/len(s)
    dataset.at[i,'d']=float(s.count('d'))/len(s)
    dataset.at[i,'e']=float(s.count('e'))/len(s)
    dataset.at[i,'f']=float(s.count('f'))/len(s)
    dataset.at[i,'g']=float(s.count('g'))/len(s)
    dataset.at[i,'h']=float(s.count('h'))/len(s)
    dataset.at[i,'i']=float(s.count('i'))/len(s)
    dataset.at[i,'j']=float(s.count('j'))/len(s)
    dataset.at[i,'k']=float(s.count('k'))/len(s)
    dataset.at[i,'l']=float(s.count('l'))/len(s)
    dataset.at[i,'m']=float(s.count('m'))/len(s)
    dataset.at[i,'n']=float(s.count('n'))/len(s)
    dataset.at[i,'o']=float(s.count('o'))/len(s)
    dataset.at[i,'p']=float(s.count('p'))/len(s)
    dataset.at[i,'q']=float(s.count('q'))/len(s)
    dataset.at[i,'r']=float(s.count('r'))/len(s)
    dataset.at[i,'s']=float(s.count('s'))/len(s)
    dataset.at[i,'t']=float(s.count('t'))/len(s)
    dataset.at[i,'u']=float(s.count('u'))/len(s)
    dataset.at[i,'v']=float(s.count('v'))/len(s)
    dataset.at[i,'w']=float(s.count('w'))/len(s)
    dataset.at[i,'x']=float(s.count('x'))/len(s)
    dataset.at[i,'y']=float(s.count('y'))/len(s)
    dataset.at[i,'z']=float(s.count('z'))/len(s)
    dataset.at[i,'0']=float(s.count('0'))/len(s)
    dataset.at[i,'1']=float(s.count('1'))/len(s)
    dataset.at[i,'2']=float(s.count('2'))/len(s)
    dataset.at[i,'3']=float(s.count('3'))/len(s)
    dataset.at[i,'4']=float(s.count('4'))/len(s)
    dataset.at[i,'5']=float(s.count('5'))/len(s)
    dataset.at[i,'6']=float(s.count('6'))/len(s)
    dataset.at[i,'7']=float(s.count('7'))/len(s)
    dataset.at[i,'8']=float(s.count('8'))/len(s)
    dataset.at[i,'9']=float(s.count('9'))/len(s)
    dataset.at[i,'-']=float(s.count('-'))/len(s)

print(dataset.head(5))

dataset['domain']=dataset['domain'].astype('str')
dataset.to_csv('alexa16-AvgCharFreq.csv', index=False)

loc = 'dga15-NgramAvgVowel.csv'
dataset = pandas.read_csv(loc)

for i in range(0,len(dataset)):
    s=dataset.at[i,'domain']
    
    dataset.at[i,'a']=float(s.count('a'))/len(s)
    dataset.at[i,'b']=float(s.count('b'))/len(s)
    dataset.at[i,'c']=float(s.count('c'))/len(s)
    dataset.at[i,'d']=float(s.count('d'))/len(s)
    dataset.at[i,'e']=float(s.count('e'))/len(s)
    dataset.at[i,'f']=float(s.count('f'))/len(s)
    dataset.at[i,'g']=float(s.count('g'))/len(s)
    dataset.at[i,'h']=float(s.count('h'))/len(s)
    dataset.at[i,'i']=float(s.count('i'))/len(s)
    dataset.at[i,'j']=float(s.count('j'))/len(s)
    dataset.at[i,'k']=float(s.count('k'))/len(s)
    dataset.at[i,'l']=float(s.count('l'))/len(s)
    dataset.at[i,'m']=float(s.count('m'))/len(s)
    dataset.at[i,'n']=float(s.count('n'))/len(s)
    dataset.at[i,'o']=float(s.count('o'))/len(s)
    dataset.at[i,'p']=float(s.count('p'))/len(s)
    dataset.at[i,'q']=float(s.count('q'))/len(s)
    dataset.at[i,'r']=float(s.count('r'))/len(s)
    dataset.at[i,'s']=float(s.count('s'))/len(s)
    dataset.at[i,'t']=float(s.count('t'))/len(s)
    dataset.at[i,'u']=float(s.count('u'))/len(s)
    dataset.at[i,'v']=float(s.count('v'))/len(s)
    dataset.at[i,'w']=float(s.count('w'))/len(s)
    dataset.at[i,'x']=float(s.count('x'))/len(s)
    dataset.at[i,'y']=float(s.count('y'))/len(s)
    dataset.at[i,'z']=float(s.count('z'))/len(s)
    dataset.at[i,'0']=float(s.count('0'))/len(s)
    dataset.at[i,'1']=float(s.count('1'))/len(s)
    dataset.at[i,'2']=float(s.count('2'))/len(s)
    dataset.at[i,'3']=float(s.count('3'))/len(s)
    dataset.at[i,'4']=float(s.count('4'))/len(s)
    dataset.at[i,'5']=float(s.count('5'))/len(s)
    dataset.at[i,'6']=float(s.count('6'))/len(s)
    dataset.at[i,'7']=float(s.count('7'))/len(s)
    dataset.at[i,'8']=float(s.count('8'))/len(s)
    dataset.at[i,'9']=float(s.count('9'))/len(s)
    dataset.at[i,'-']=float(s.count('-'))/len(s)

print(dataset.head(5))

dataset['domain']=dataset['domain'].astype('str')
dataset.to_csv('dga16-AvgCharFreq.csv', index=False)