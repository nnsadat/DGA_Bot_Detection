# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 21:30:28 2018

@author: User
"""

import pandas
import numpy
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

loc = 'combinedDataset.csv'
dataset = pandas.read_csv(loc)
pandas.set_option('display.max_columns',80)
print(dataset.head(3))
array = dataset.values
X = array[:,2:67]
Y = array[:,1]

test = SelectKBest(score_func=chi2, k=6)
fit = test.fit(X, Y)

numpy.set_printoptions(precision=3)
print(fit.scores_)
features = fit.transform(X)

print(features[0:3,:])