# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 01:14:33 2018

@author: User
"""

import pandas
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import matthews_corrcoef
import _pickle as pkl

loc = 'combinedDataset.csv'
dataset = pandas.read_csv(loc)
dataset=dataset[['bigramNS','trigramNS','bigramWt','trigramWt','bigramEntropy1','trigramEntropy1','a','e','i','o','u','-','0','1','2','3','4','5','6','7','8','9','class']].copy()#38
print(dataset.shape)

pandas.set_option('display.max_columns',80)

print(dataset.groupby('class').size())
array = dataset.values
X = array[:,0:22]
Y = array[:,22]
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)
seed = 7
scoring = 'accuracy'

models = []
models.append(('LR', LogisticRegression()))
models.append(('KNN5', KNeighborsClassifier(5)))
models.append(('KNN10', KNeighborsClassifier(10)))
models.append(('KNN15', KNeighborsClassifier(15)))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', LinearSVC()))
models.append(('RF10',RandomForestClassifier(10)))
models.append(('RF20',RandomForestClassifier(20)))
models.append(('RF30',RandomForestClassifier(30)))
models.append(('RF40',RandomForestClassifier(40)))
models.append(('RF50',RandomForestClassifier(50)))
results = []
names = []

for name, model in models:
	kfold = model_selection.KFold(n_splits=10, random_state=seed)
	cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
	results.append(cv_results)
	names.append(name)
	msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
	print(msg)

fig = plt.figure()
fig.suptitle('Algorithm Comparison')
fig.set_size_inches(9, 9)
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.show()

rf = RandomForestClassifier(10)
rf.fit(X_train, Y_train)
predictions = rf.predict(X_validation)
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions,labels=["dga", "legit"]))
print(classification_report(Y_validation, predictions))
print(matthews_corrcoef(Y_validation, predictions) )
with open('my_rf_classifier10.pkl', 'wb') as fid:
    pkl.dump(rf, fid)   

rf = RandomForestClassifier(20)
rf.fit(X_train, Y_train)
predictions = rf.predict(X_validation)
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))
print(matthews_corrcoef(Y_validation, predictions) )
with open('my_rf_classifier20.pkl', 'wb') as fid:
    pkl.dump(rf, fid)   
    
rf = RandomForestClassifier(30)
rf.fit(X_train, Y_train)
predictions = rf.predict(X_validation)
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))
print(matthews_corrcoef(Y_validation, predictions) )
with open('my_rf_classifier30.pkl', 'wb') as fid:
    pkl.dump(rf, fid)   
    
rf = RandomForestClassifier(40)
rf.fit(X_train, Y_train)
predictions = rf.predict(X_validation)
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))
print(matthews_corrcoef(Y_validation, predictions) )
with open('my_rf_classifier40.pkl', 'wb') as fid:
    pkl.dump(rf, fid)   
    
rf = DecisionTreeClassifier()
rf.fit(X_train, Y_train)
predictions = rf.predict(X_validation)
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))
print(matthews_corrcoef(Y_validation, predictions) )
with open('my_rf_classifierDT.pkl', 'wb') as fid:
    pkl.dump(rf, fid)


