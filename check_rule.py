#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 22:06:45 2018

@author: raja
"""


import pandas as pd
import numpy as np
import re
import rules

df_x=pd.read_csv('/home/raja/Desktop/ce/Nov_08/text_alone_CE_1003.csv', header=None, delimiter="\t")



r10='caused|causes|generated|generates|makes|triggered|triggers|radiated|radiates|produced|produces|emmited|emits|created|creates|cause|generate|make|trigger|radiate|produce|emit|create|made'
r20='(result|causes|leads|source|due|cause|lead)\W+(?:\w+\W+){1,5}?(a|in|of|to)'
r30=r'(caused|generated|triggeres|produced|damaged).* (by)'
r40=r'(from|after|emit)'

kf=[]
ce=[]
"""
for text in df_x[0]:
    k=[0,0,0,0]
    if re.search(r10,text):
        k[0]=1
        
    if re.search(r20,text):
        k[1]=1
        
    if re.search(r30,text):
        k[2]=1
        
    if re.search(r40,text):
        k[3]=1
        
        
    kf.append(k)
"""

for text in df_x[0]:
    k=[0,0,0,0]
    cause_effect_one=[]
    if re.search(r30,text):
        k[2]=1
        cause_effect_one=rules.rule3(text)
    else: 
        if re.search(r20,text):
            k[1]=1
            cause_effect_one=rules.rule2(text)
        
        else:
            
            if re.search(r10,text):
                k[0]=1
                cause_effect_one=rules.rule1(text)
            else:    
                
                    
                if re.search(r40,text):
                    k[3]=1
                    cause_effect_one=rules.rule4(text)
    kf.append(k)
    ce.append(cause_effect_one)




























