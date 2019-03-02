#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 03:23:36 2018

@author: raja
"""

from nltk.corpus import wordnet as wn

word='bond'

syno=[]

for syn in wn.synsets(word):
    for l1 in syn.lemmas():
       syno.append(l1.name()) 
print(list(syno))



def get_hyponyms(synset):
    hyponyms = set()
    for hyponym in synset.hyponyms():
        hyponyms |= set(get_hyponyms(hyponym))
    return hyponyms | set(synset.hyponyms())


hypo=[]

for syn in wn.synsets(word):
    for h1 in syn.hyponyms():
        hypo.append(h1.names())
        
print(hypo)