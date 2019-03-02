#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 21:14:51 2018

@author: raja
"""


import pandas as pd
import numpy as np
df = pd.read_csv('/home/raja/Desktop/ce/oct_26/TRAIN_FILE.TXT', header=None, delimiter="\t")

d2=df.iloc[::3][1]

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


x_e1e2_ce = d2[y==1]

x_e1e2_ce.to_csv('text_x_e1e2_CE_only.csv', index=False, header=False)

df_pos = pd.read_csv('/home/raja/Desktop/ce/oct_27/pos_tree.csv', header=None, delimiter="\t")


x_pos_ce =df_pos[y==1]

x_pos_ce.to_csv('pos_CE_only.csv', index=False, header=False)

