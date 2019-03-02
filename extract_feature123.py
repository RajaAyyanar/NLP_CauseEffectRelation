#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 11:10:19 2018

@author: raja
"""

import pandas as pd
import numpy as np
import nltk
from nltk.tree import ParentedTree
import find_leaves
import find_path

import re

df = pd.read_csv('text_all_8000_with_e1e2.csv', header=None, delimiter="\t")
df_pos=pd.read_csv('pos_all_8000.csv', header=None, delimiter="\t")
df_text = pd.read_csv('text_alone.csv', header=None, delimiter="\t")

s_pos=nltk.pos_tag(nltk.word_tokenize(df_text[0][5]))

cause_set=[]
effect_set=[]
between_set=[]
before_set_pos=[]
between_set_pos=[]
after_set_pos=[]
path_set=[]


pattern1 = r'<e1>(.*?)</e1>'
pattern2 = r'<e2>(.*?)</e2>'
between_pattern= r'</e1>(.*?)<e2>'
sen=0;
for s in df[0]:    
    #s = df[0][sen]
    e1=re.search(pattern1, s).group(1)
    e2=re.search(pattern2, s).group(1)
    cause_set.append(e1)
    effect_set.append(e2)
    between_one=re.search(between_pattern, s).group(1)
    between_set.append(between_one)
    
    
    s2=df_text[0][sen]
    
    f1=s2.partition(e1+between_one+e2)
    first=f1[0]
    last=f1[2]
    bet=f1[1]
    b_len = len(first.split())
    l_len = len(last.split())
    bt_len = len(bet.split())
    s_pos=nltk.pos_tag(nltk.word_tokenize(s2))
    sd=pd.DataFrame(s_pos)
    sd[1]=find_leaves.pos_text2num(sd)
    before_pos = sd[1][0:b_len+1].values.tolist()
    between_pos = sd[1][b_len:b_len+bt_len+1].values.tolist()
    after_pos = sd[1][b_len+bt_len-1:].values.tolist()
       
    
    before_set_pos.append(before_pos)
    between_set_pos.append(between_pos)
    after_set_pos.append(after_pos)    
    
    
    s2_pos=df_pos[0][sen]
    if  sen==3044 or sen==4218 or sen==4218 or sen==4611 or sen==4783 or sen==5233 or sen==6372 or sen==7097:
        path=[]
    else:
        path=find_path.find_path1(s2_pos,e1,e2)
    path_set.append(path)
    
    sen=sen+1
    
    
all_cause = pd.DataFrame(cause_set).fillna('0')
all_effect = pd.DataFrame(effect_set).fillna('0')
all_between_words =pd.DataFrame(between_set).fillna('0')
all_paths_e1e2 =pd.DataFrame(path_set).fillna('0')

all_before_set_pos=pd.DataFrame(before_set_pos).fillna('0')
all_between_set_pos=pd.DataFrame(between_set_pos).fillna('0')
all_after_set_pos=pd.DataFrame(after_set_pos).fillna('0')


features1= all_before_set_pos.iloc[:,:20]
features2= all_between_set_pos.iloc[:,:20]
features3= all_after_set_pos.iloc[:,:20]
features4= all_paths_e1e2.iloc[:,:10]
features4=find_leaves.pos_text2num22(features4)

final_features=pd.concat([features1,features2,features3,features4], axis=1)

final_features.to_csv('final_features_8000x70.csv',index=False,header=False)






def metrics(labels, predictions):
    true_pos, true_neg, false_pos, false_neg = 0, 0, 0, 0
    for i in range(len(labels)):
        true_pos += int(labels[i] == 1 and predictions[i] == 1)
        true_neg += int(labels[i] == 0 and predictions[i] == 0)
        false_pos += int(labels[i] == 0 and predictions[i] == 1)
        false_neg += int(labels[i] == 1 and predictions[i] == 0)
    precision = true_pos / (true_pos + false_pos)
    recall = true_pos / (true_pos + false_neg)
    Fscore = 2 * precision * recall / (precision + recall)
    accuracy = (true_pos + true_neg) / (true_pos + true_neg + false_pos + false_neg)

    print("Precision: ", precision)
    print("Recall: ", recall)
    print("F-score: ", Fscore)
    print("Accuracy: ", accuracy)






