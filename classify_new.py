#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 00:21:17 2018

@author: raja
"""


import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets
import sklearn

from sklearn import svm

X=np.load('x_matrix_2000x150.npy')
y=np.load('y_matrix_2000.npy')



from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=2,shuffle=True)



neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(X_train, y_train) 
#post_probs = lda_clf.predict_proba(X_test)
y_pred = neigh.predict(X_test)

from sklearn import metrics
print("KNN model accuracy(in %):", metrics.accuracy_score(y_test, y_pred)*100)


confusion1=sklearn.metrics.confusion_matrix(y_test, y_pred, labels=None, sample_weight=None)



svm1 = svm.SVC()
svm1.fit(X_train, y_train) 
#post_probs = lda_clf.predict_proba(X_test)
y_pred = svm1.predict(X_test)

from sklearn import metrics
print("SVM model accuracy(in %):", metrics.accuracy_score(y_test, y_pred)*100)


confusion2=sklearn.metrics.confusion_matrix(y_test, y_pred, labels=None, sample_weight=None)
