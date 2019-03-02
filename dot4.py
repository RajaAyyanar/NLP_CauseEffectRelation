#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 22:06:37 2018

@author: raja
"""

import dot3
import numpy as np

import pandas as pd
df = pd.read_csv('pos_tree_number.csv', header=None,delimiter="\t")

pre=np.zeros((8000,30))
post=np.zeros((8000,30))
    
for h1 in range(0,len(df)):
    textt1=df[0][h1]
    
    pre_sent, aft_sent = dot3.path2beforeAfterLength(textt1)
    pre_sent=pre_sent.tolist()
    aft_sent=aft_sent.tolist()
    
    #To extend maximum word in a sentence to 30
    max_len=30
    pre_sent.extend([0] * (max_len - len(pre_sent)))
    aft_sent.extend([0] * (max_len - len(aft_sent)))
    a4=np.array(pre_sent)
    a5=np.array(aft_sent)

    
    pre[h1,:]=a4
    post[h1,:]=a5
    
    

    