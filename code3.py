#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 12:35:01 2018

@author: raja
"""

taggs1 = ["CC","CD","DT","EX","FW","IN","JJ","JJR","JJS","LS","MD",
        "NN","NNS","NNP","NNPS","PDT","POS","PRP","PRP$","RB","RBR","RBS",
        "RP","SYM","TO","UH","VB","VBD","VBG","VBN","VBP","VBZ","WDT",
        "WP","WP$","WRB"]
taggs2 =["ADJP","ADVP","CONJP","FRAG","INTJ","LST","NAC","NP","NX",
        "PP","PRN","PRT","QP","RRC","UCP","VP","WHADJP","WHAVP","WHNP","WHPP","X","WHADVP"]

taggs3 =["S" , "SBAR", "SBARQ", "SINV","SQ"]

taggs4 = [".",",",":","''",'``',"$","#","-LRB-","-RRB-","NONE","*","T","NUL"]
          
taggs5=["-TMP"]

taggs =taggs1+taggs2+taggs3+taggs4+taggs5

taggs.sort(key = len)
taggs.reverse()

import pandas as pd
df = pd.read_csv('pos_tree.csv', header=None,delimiter="\t")
df=df[0].str.replace('"',' ')
new=df

i=1;
for t in taggs:    
    new=new.str.replace(t,str(i))
    i=i+1
    
    
new.to_csv('pos_tree_number.csv',index=False,header=False)