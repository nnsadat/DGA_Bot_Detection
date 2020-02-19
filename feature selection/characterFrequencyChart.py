# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 23:30:05 2018

@author: User
"""

import pandas
import matplotlib.pyplot as plt

loc = 'combinedDataset.csv'
dataset = pandas.read_csv(loc)

for i in range(0,len(dataset)):
    s=dataset.at[i,'domain']
    dataset.at[i,'a']=s.count('a')
    dataset.at[i,'b']=s.count('b')
    dataset.at[i,'c']=s.count('c')
    dataset.at[i,'d']=s.count('d')
    dataset.at[i,'e']=s.count('e')
    dataset.at[i,'f']=s.count('f')
    dataset.at[i,'g']=s.count('g')
    dataset.at[i,'h']=s.count('h')
    dataset.at[i,'i']=s.count('i')
    dataset.at[i,'j']=s.count('j')
    dataset.at[i,'k']=s.count('k')
    dataset.at[i,'l']=s.count('l')
    dataset.at[i,'m']=s.count('m')
    dataset.at[i,'n']=s.count('n')
    dataset.at[i,'o']=s.count('o')
    dataset.at[i,'p']=s.count('p')
    dataset.at[i,'q']=s.count('q')
    dataset.at[i,'r']=s.count('r')
    dataset.at[i,'s']=s.count('s')
    dataset.at[i,'t']=s.count('t')
    dataset.at[i,'u']=s.count('u')
    dataset.at[i,'v']=s.count('v')
    dataset.at[i,'w']=s.count('w')
    dataset.at[i,'x']=s.count('x')
    dataset.at[i,'y']=s.count('y')
    dataset.at[i,'z']=s.count('z')
    dataset.at[i,'0']=s.count('0')
    dataset.at[i,'1']=s.count('1')
    dataset.at[i,'2']=s.count('2')
    dataset.at[i,'3']=s.count('3')
    dataset.at[i,'4']=s.count('4')
    dataset.at[i,'5']=s.count('5')
    dataset.at[i,'6']=s.count('6')
    dataset.at[i,'7']=s.count('7')
    dataset.at[i,'8']=s.count('8')
    dataset.at[i,'9']=s.count('9')
    dataset.at[i,'-']=s.count('-')
    dataset.at[i,'.']=s.count('.')
    
    
pandas.set_option('display.max_columns',40)
dataset.head(5)
dl=dataset.loc[dataset['class']=='legit']#79035
dd=dataset.loc[dataset['class']=='dga']
dl=dl[['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','.','-']].copy()
dd=dd[['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','.','-']].copy()
legitVar=dl.mean()
dgaVar=dd.mean()
x=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','.','-']
fig = plt.gcf()
fig.set_size_inches(9, 9)

plt.plot(dgaVar[0:39],'ro--',legitVar[0:39],'bx--')
plt.show()
fig.savefig('varcharfreq.png')

