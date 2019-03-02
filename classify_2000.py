#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 14:21:34 2018

@author: raja
"""


import pandas as pd
import numpy as np

X = np.genfromtxt('final_features_8000x70.csv', delimiter=',')
where_are_NaNs = np.isnan(X)
X[where_are_NaNs] = 0


y2=np.genfromtxt('target_y_CE_8000.csv')


X1=X[y2==1]
X0=X[y2==0]
Y0=y2[y2==0]
Y1=y2[y2==1]


X=np.concatenate((X1,X0[0:1000,:]),axis=0)
y=np.concatenate((Y1,Y0[0:1000]),axis=0)


import numpy as np

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

y_ = y.reshape(-1, 1)
# One Hot encode the class labels
encoder = OneHotEncoder(sparse=False)
y = encoder.fit_transform(y_)
#print(y)

# Split the data for training and testing
train_x, test_x, train_y, test_y = train_test_split(X, y, test_size=0.20)

# Build the model

model = Sequential()

model.add(Dense(128, input_shape=(70,), activation='relu', name='fc1'))
model.add(Dense(64, activation='relu', name='fc2'))
model.add(Dense(10, activation='relu', name='fc3'))
model.add(Dense(2, activation='softmax', name='output'))

# Adam optimizer with learning rate of 0.001
optimizer = Adam(lr=0.001)
model.compile(optimizer, loss='categorical_crossentropy', metrics=['accuracy'])

print('Neural Network Model Summary: ')
print(model.summary())

# Train the model
model.fit(train_x, train_y, verbose=2, batch_size=5, epochs=200)

# Test on unseen data

results = model.evaluate(test_x, test_y)

print('Final test set loss: {:4f}'.format(results[0]))
print('Final test set accuracy: {:4f}'.format(results[1]))









