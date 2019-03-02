#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 00:35:15 2018

@author: raja
"""
from __future__ import print_function
import numpy as np
import pandas as pd

X2=np.load('final_num_x.npy')

X=X2[:,0:50,0:25]
y= pd.read_csv('test_y.csv', header=None, delimiter="\t")
y[0]=y[0].str.replace("1","2")
kk=y[0].unique().tolist()
kk.sort(key=len)
y=y[0].str.replace("1","2")
"""
i=0;
for t in kk:    
    y=y.replace(t,str(i))
    i=i+1
"""

i=0
for t in kk:
    if i==1:
        y=y.replace(t,"1")
    else:
        y=y.replace(t,'0')    
    i=i+1
    

y=y.values
y=y.astype(np.int)



from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1,shuffle=True)




import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K

batch_size = 40
num_classes = 2
epochs = 20

m_rows, m_cols = 50,25

x_train = x_train.reshape(x_train.shape[0], m_rows, m_cols, 1)
x_test = x_test.reshape(x_test.shape[0], m_rows, m_cols, 1)
input_shape = (m_rows, m_cols, 1)


x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
#x_train /= 77
#x_test /= 77
print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

# convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)


model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3),
                 activation='relu',
                 input_shape=input_shape))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.25))
model.add(Dense(num_classes, activation='softmax'))

model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy'])

model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=epochs,
          verbose=1,
          validation_data=(x_test, y_test))
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])


y_pred=model.predict(x_test)
y_pred[y_pred>0.5]=1
y_pred[y_pred<=0.5]=0

print(sum(y_pred-y_test))


























