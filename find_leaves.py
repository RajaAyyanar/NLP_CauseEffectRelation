#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 11:29:52 2018

@author: raja
"""
import pandas as pd

from nltk.tree import ParentedTree
def pos_text2num(df):
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
    

    
    df=df[1].str.replace('"',' ')
    new=df
    
    i=1;
    for t in taggs:    
        new=new.str.replace(t,str(i))
        i=i+1
        
    return new

def pos_text2num22(df):
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
    
    
    df=df.replace('"',' ')
    new=df
    
    i=1;
    for t in taggs:    
        new=new.replace(t,str(i))
        i=i+1
        
    return new