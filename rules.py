#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 22:44:07 2018

@author: raja
"""


import re
import spacy
import pandas as pd
import numpy as np

nlp = spacy.load('en_core_web_sm')

def rule1(text):
    
    doc = nlp(text)
    
    
    f1=[]
    for token in doc:
        #print(token.text, token.dep_, token.head.text)
        a=[token.text, token.dep_, token.head.text]          
        f1.append(a)
        
    dep_parser=pd.DataFrame(f1)
    
    
    r1_condition="""caused|causes|generated|generates|makes|triggered|triggers|radiated|radiates|produced|produces|emmited|emits|created|creates|cause|generate|make|trigger|radiate|produce|emit|create|made"""
    
    our_str=r1_condition
    all_verb = our_str.replace('|', ' ')
    all_verb = all_verb.split()
    
    if re.search(r1_condition,text):
        a=re.search(r1_condition,text)
        word_present=a.group()
    
    temp= dep_parser[2]==word_present
    CE=dep_parser[temp]
    
        
    temp1= CE[1]=="nsubj"
    
    temp2=CE[temp1]
    Cause=temp2[0].values.tolist()
    
    temp3= CE[1]=="dobj"
    temp4=CE[temp3]
    Effect=temp4[0].values.tolist()
    
    CE_list=[]
    if len(Cause)*len(Effect) > 0:
        CE_list=[Cause[0],Effect[0]]

        
    return CE_list


def rule2(text):
    #text=u"A wind lead to kill him in jungle"
    #text="A secret for avoiding weight gain due to stress is the use of adaptogens"
    doc = nlp(text)
    
    r2_condition='(result|cause|lead|source|due|causes|leads)\W+(?:\w+\W+){1,5}?(a|in|of|to)'
    rule2_verb=['result','cause','lead','source','due']
    rule2_prep=['a','in','of','to']
    
    
    
    f2=[]
    if re.search(r2_condition,text):
        a=re.search(r2_condition,text)
        f2=a.group().split()
        
    if len(f2)==0:
        return f2
                        
    one_verb=f2[0]
    one_pre=f2[1]            
        
    """
    if len(f2)==0:
        return "NOTHING there"
    """
    
    
    
    f1=[]
    for token in doc:
        #print(token.text, token.dep_, token.head.text)
        a=[token.text, token.dep_, token.head.text]          
        f1.append(a)
        
    dep_parser=pd.DataFrame(f1)
    
    
    temp=dep_parser[1]=='nsubj'
    CE=dep_parser[temp]
    CE2=CE.values.T.tolist()
    Cause=[]
    if len(CE)==0:
        return Cause
    
    if CE2[2][0]==one_verb or CE2[2][0]==one_verb+'s' or CE2[2][0]==one_verb+'es' :
        Cause=CE2[2][0]
    
    temp=dep_parser[2]==one_pre
    EF=dep_parser[temp]
    EF2= EF.values.T.tolist()
    
    #if (EF2[1][0]==r'aux') or (EF2[1][0]==r'prep'):
    #    Effect=EF2[2][0]
    
        
    if not len(EF)==0:
        Effect=EF2[0][0]
    else:
        Effect=[]
    CE_list=[Cause,Effect]
    return CE_list



def rule3(text):
    r3_condition=r'(caused|generated|triggered|produced|damaged).* (by) '
    #text='The fire was caused by the bombing'
    doc = nlp(text)
    
    f2=[]
    if re.search(r3_condition,text):
        a=re.search(r3_condition,text)
        f2=a.group().split()
    
    
    
    f1=[]
    for token in doc:
        #print(token.text, token.dep_, token.head.text)
        a=[token.text, token.dep_, token.head.text]          
        f1.append(a)
        
    dep_parser=pd.DataFrame(f1)
    
    
    temp=dep_parser[1]=='agent'
    temp2=dep_parser[temp]
    temp3=dep_parser[2]=='by'
    temp4=dep_parser[temp3]
    Cause=temp4[0].values.tolist()
    
    
    temp5=dep_parser[1]=='nsubjpass'
    temp6=dep_parser[temp5]
    Effect=temp6[0].values.tolist()
    
    if len(Effect)==0:
        
        temp5=dep_parser[1]=='nsubj'
        temp6=dep_parser[temp5]
        Effect=temp6[0].values.tolist()
    
    CE_list=[]
    if len(Cause)>0 and len(Effect)>0 :
        CE_list=[Cause[0],Effect[0]]
        
    return CE_list    







def rule4(text):
    r4_condition=r'(from|after|emit)'

    doc = nlp(text)
    
    
    f2=[]
    if re.search(r4_condition,text):
        a=re.search(r4_condition,text)
        f2=a.group().split()
    
    
    f1=[]
    for token in doc:
        #print(token.text, token.dep_, token.head.text)
        a=[token.text, token.dep_, token.head.text,token.head.pos_]          
        f1.append(a)
        
    dep_parser=pd.DataFrame(f1)
    
    
    temp=dep_parser[1]=='pobj'
    temp2=dep_parser[temp]
    temp3=temp2[2]==f2[0]
    temp4=temp2[temp3]
    if len(temp4)==0:
        temp3=temp2[2]=='from'
        temp4=temp2[temp3]
    
    if len(temp4)==0:
            
        temp=dep_parser[1]=='dobj'
        temp2=dep_parser[temp]
        temp3=temp2[2]==f2[0]
        temp4=temp2[temp3]
        if len(temp4)==0:
            temp3=temp2[2]=='from'
            temp4=temp2[temp3]
    
    
    
    Cause=temp4[0].values.tolist()
    if len(Cause)==0:
        Cause=[[]]
        
        
        
    temp=dep_parser[1]=='prep'
    temp2=dep_parser[temp]
    temp3=temp2[0]==f2[0]
    
    temp4=temp2[temp3]
    CE_list=[]
    
    if not len(temp4)==0:
        temp4=temp4.head(1)
                
        if (temp4[3]=='NOUN').bool():
            Effect=temp4[2].values.tolist()
            CE_list=[Cause[0],Effect[0]]
        
        elif (temp4[3]=='VERB').bool():
            temp5=dep_parser[2]==temp4[2].values.tolist()[0]
            temp6=dep_parser[temp5]
            
            temp7=temp6[1]=='nsubj' 
            temp8=temp6[temp7]   
            Effect=temp8[0].values.tolist()
            if not len(Effect)==0:
                CE_list=[Cause[0],Effect[0]]
                
            else:
                temp7=temp6[1]=='dobj' 
                temp8=temp6[temp7]   
                Effect=temp8[0].values.tolist()
                
                if len(Effect)==0:
                    CE_list=[]
                    
                else:
                    CE_list=[Cause[0],Effect[0]]
                              
    return CE_list




def rule5(text):
    #text="Heat, wind and smoke cause flight delays."
    doc = nlp(text)
    
    
    f1=[]
    for token in doc:
        #print(token.text, token.dep_, token.head.text)
        a=[token.text, token.dep_, token.head.text]          
        f1.append(a)
        
    dep_parser=pd.DataFrame(f1)
    
    
    r1_condition='cause|generate|make|trigger|radiate|produce|emit|create|made'
    our_str=r1_condition
    all_verb = our_str.replace('|', ' ')
    all_verb = all_verb.split()
    
    if re.search(r1_condition,text):
        a=re.search(r1_condition,text)
        word_present=a.group()
    
    temp= dep_parser[2]==word_present
    CE=dep_parser[temp]
    
    temp1= CE[1]=="nsubj"
    
    temp2=CE[temp1]
    Cause=temp2[0].values.tolist()
    
    temp3= CE[1]=="dobj"
    temp4=CE[temp3]
    Effect=temp4[0].values.tolist()
    
    #CE_list=[Cause[0],Effect[0]]
    
    m_temp1=dep_parser[1]=='conj'
    m_temp2=dep_parser[m_temp1]
    
    m_cause=[]
    
    ccheck= Cause[0]
    m_cause.append(ccheck)
    for onec in range(0,len(m_temp2)):
        df_c=m_temp2[m_temp2[2]==ccheck]
        if len(df_c)>0:
            ccheck=(df_c[0]).values.tolist()[0]
            m_cause.append(ccheck)
    
    
    m_effect=[]
    echeck= Effect[0]
    m_effect.append(echeck)
    for onec in range(0,len(m_temp2)):
        df_x=m_temp2[m_temp2[2]==echeck]
        if len(df_x)!=0:
            echeck=(df_x[0]).values.tolist()[0]
            m_effect.append(echeck)
    
    return [m_cause,m_effect]





