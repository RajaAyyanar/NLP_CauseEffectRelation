#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 14:55:52 2018

@author: raja
"""
import code2
import numpy as np

import pandas as pd
df = pd.read_csv('pos_tree_number.csv', header=None,delimiter="\t")

i=0
map1=[]
for textt in df[0]:
    map2=code2.parser2path(textt)
    map1.append(map2)
    i=i-1
    if i%10==0:
        print(i)


#max_len = max(len(sublist) for sublist in map1_1)
max_len=100
for sublist in map1:
    sublist.extend([["0"]] * (max_len - len(sublist)))



m1=0
for j in range(0,len(map1)):
    map1_1=map1[j]
    #max_len = max(len(sublist) for sublist in map1_1)
    max_len=30
    for sublist in map1_1:
        sublist.extend(["0"] * (max_len - len(sublist)))
    map1[j]=map1_1
    j+=1

    

final_x=np.array(map1)
np.save('final_text.npy',final_x)

f1_x = final_x.astype(np.int)
np.save('final_num_x.npy',f1_x)

