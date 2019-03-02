#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 13:05:59 2018

@author: raja
"""

import pandas as pd
df = pd.read_csv('text_alone.csv', header=None,delimiter="\t")

from nltk.parse.corenlp import CoreNLPParser
parser = CoreNLPParser(url='http://localhost:9010')

i=len(df[0])
pp=[]
for one_t in df[0]:
    text=one_t    
    #text =  "The runner scored from second on a base hit"
    
    parse123 = next(parser.parse_text(text))
    #Flattenning the tree
    parse_string = ' '.join(str(parse123).split()) 
    pp.append(parse_string)
    i=i-1
    if i%10==0:
        print(i)
        
ppdata=pd.DataFrame(pp)
ppdata.to_csv('pos_tree1.csv',index=False,header=False)