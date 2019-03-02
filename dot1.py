#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 21:29:20 2018

@author: raja
"""

import numpy as np
import pandas as pd

X2=np.load('/home/raja/Desktop/ce/oct_29/x_new_features8000x150.npy')

X=X2
y= pd.read_csv('/home/raja/Desktop/ce/oct_28/test_y.csv', header=None, delimiter="\t")
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

####FOR 1000 + 1000 split of two classes

new_x1=[]
new_x0=[]
new_y1=[]
new_y0=[]

for p in range(0,len(y)):
    if y[p]==1:
        new_x1.append(X[p,:])
        new_y1.append(y[p])
    else:
        new_x0.append(X[p,:])
        new_y0.append(y[p])

X=np.array(new_x1+new_x0)
y=np.array(new_y1+new_y0)

X=X[0:2000,:]
y=y[0:2000]


np.savetxt('X_new_features_2000x150.csv', X, delimiter=',',fmt="%d")
np.savetxt('y_new_features_2000.csv', y, delimiter=',',fmt="%d")

np.save('x_matrix_2000x150.npy',X)
np.save('y_matrix_2000.npy',y)


