#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 20:45:34 2018

@author: raja
"""

import pandas as pd
import numpy as np
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
y=pd.DataFrame(y)
y.to_csv('target_y_CE_8000.csv',index=False,header=False)
