#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 21:26:16 2018

@author: raja
"""

from nltk.corpus import wordnet as wn

def find_synonyms(word):
    #word='bond'
    syno=[]
    for syn in wn.synsets(word):
        for l1 in syn.lemmas():
           syno.append(l1.name()) 
    return syno
    
    
    
import pandas as pd
import re
import find_path

df = pd.read_csv('text_all_8000_with_e1e2.csv', header=None, delimiter="\t")
df_pos=pd.read_csv('pos_all_8000.csv', header=None, delimiter="\t")

cause_set=[]
effect_set=[]
between_set=[]
e1_synonym_set=[]
e2_synonym_set=[]
path_set=[]
feature_set=[]


pattern1 = r'<e1>(.*?)</e1>'
pattern2 = r'<e2>(.*?)</e2>'
between_pattern= r'</e1>(.*?)<e2>'
sen=0;
for s in df[0]:    
    #s = df[0][11]
    e1=re.search(pattern1, s).group(1)
    e2=re.search(pattern2, s).group(1)
    cause_set.append(e1)
    effect_set.append(e2)
    between_one=re.search(between_pattern, s).group(1)
    between_set.append(between_one)
    e1_syn=find_synonyms(e1)
    e2_syn=find_synonyms(e2) 
    e1_syn=' '.join(e1_syn)
    e2_syn=' '.join(e2_syn)
    e1_synonym_set.append(e1_syn)
    e2_synonym_set.append(e2_syn)
    s2=df_pos[0][sen]
    if sen==3044 or sen==4218 or sen==4218 or sen==4611 or sen==4783 or sen==5233 or sen==6372 or sen==7097:
        path=[]
    else:
        path=find_path.find_path1(s2,e1,e2)
    path_set.append(path)
    path=' '.join(path)
    feature1=e1+" "+e2+" "+e1_syn+" "+e2_syn+" "+path
    feature_set.append(feature1)    
    sen=sen+1
    
    
all_cause = pd.DataFrame(cause_set)
all_effect = pd.DataFrame(effect_set)
all_between_words =pd.DataFrame(between_set)
all_e1_synonyms = pd.DataFrame(e1_synonym_set)
all_e2_synonyms = pd.DataFrame(e2_synonym_set)
all_paths_e1e2 =pd.DataFrame(path_set)
all_features_8000 =pd.DataFrame(feature_set)
    
"""
    
all_cause.to_csv('CE_all_cause.csv',index=False,header=False)
all_effect.to_csv('CE_all_effect.csv',index=False,header=False)
all_between_words.to_csv('CE_all_between_words.csv',index=False,header=False)
all_e1_synonyms.to_csv('CE_all_e1_synonyms.csv',index=False,header=False)
all_e2_synonyms.to_csv('CE_all_e2_synonyms.csv',index=False,header=False)
all_paths_e1e2.to_csv('CE_all_path_e1e2.csv',index=False,header=False)
"""

all_features_8000.to_csv('all_features_8000.csv',index=False,header=False)
