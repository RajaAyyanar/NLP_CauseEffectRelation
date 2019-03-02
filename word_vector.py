#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 14:07:18 2018

@author: raja
"""

import gensim
from nltk.corpus import brown

model = gensim.models.Word2Vect



from gensim.models import KeyedVectors
filename = '/home/raja/NLP_lib/wordVector_corpus/GoogleNews-vectors-negative300.bin'
model = KeyedVectors.load_word2vec_format(filename, binary=True)


