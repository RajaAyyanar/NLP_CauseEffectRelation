#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 20:48:04 2018

@author: raja
"""
import pandas as pd
import numpy as np

X= pd.read_csv('text_alone.csv', header=None, delimiter="\t")
y= pd.read_csv('target_y_CE_8000.csv', header=None, delimiter="\t")
X_e1e2= pd.read_csv('text_all_8000_with_e1e2.csv', header=None, delimiter="\t")


mails=pd.DataFrame()
mails['message']=X[0]
mails['label']=y[0]


trainIndex, testIndex = list(), list()
for i in range(mails.shape[0]):
    if np.random.uniform(0, 1) < 0.80:
        trainIndex += [i]
    else:
        testIndex += [i]
trainData = mails.loc[trainIndex]
testData = mails.loc[testIndex]
test_e1e2= X_e1e2.loc[testIndex]
train_e1e2=X_e1e2.loc[trainIndex]


trainData.reset_index(inplace = True)
trainData.drop(['index'], axis = 1, inplace = True)
trainData.head()

testData.reset_index(inplace = True)
testData.drop(['index'], axis = 1, inplace = True)
testData.head()


train_e1e2.reset_index(inplace = True)
train_e1e2.drop(['index'], axis = 1, inplace = True)


test_e1e2.reset_index(inplace = True)
test_e1e2.drop(['index'], axis = 1, inplace = True)



trainData['label'].value_counts()
testData['label'].value_counts()


"""
trainData.to_csv('train.csv',index=False,header=False)
testData.to_csv('test.csv',index=False,header=False)
sen==26 or sen==212 or sen==488 or sen==592 or sen==786 or sen==994 or sen==1009 or sen==1057 or sen==1287 or sen==1292 or sen==1425 or sen==1558 or sen==1712 or sen==1719 or sen==1789 or
"""



full=' '.join(trainData['message'])
line=full

for char in """ !@#$%^&*()_+|}{":?><~/.,;'[]=-\ """ :  
    line = line.replace(char,' ') 

full=line.lower()
all_words = full.split()
s=all_words
uniq_s= list(set(s))
sorted_uniq = sorted(uniq_s)




















