#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 21:35:28 2018

@author: raja
"""


import numpy as np
import pandas as pd

X2=np.load('/home/raja/Desktop/ce/oct_29/x_matrix.npy')
y2=np.load('/home/raja/Desktop/ce/oct_29/y_matrix.npy')


r,c,d = np.shape(X2)
c=30
new_dim_X =np.zeros((r,c,5))


for i in range(0,r):
    for j in range(0,c):
        one=X2[i,j,:]
        prime=np.array([2,3,5,7,11,13,17,19,23,29,31,37,41,
                        43,47,53,59,61,67,71,73,79,83,89,97])
        a1=j                    #Location of word in sentence
        a2=np.count_nonzero(one)  #number of layers
        a3=np.dot(one,prime)    #multiply with prime
        new_dim_X[i,j,:]=np.array([a1,a2,a3,0,0])
        
        
new_dim_X[:,:,3]=pre
new_dim_X[:,:,4]=post


np.save('x_new_features.npy',new_dim_X)
new2=np.reshape(new_dim_X, (8000,150))
new2=new2.astype(int)
np.savetxt('new_features_x.csv', new2, delimiter=',',fmt="%d")

np.save('x_new_features8000x150.npy',new2)
