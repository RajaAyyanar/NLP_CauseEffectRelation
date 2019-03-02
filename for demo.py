#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 21:56:24 2018

@author: raja
"""

import pandas as pd
import re
from wordcloud import WordCloud


df = pd.read_csv('/home/raja/Desktop/test.txt', header=None, delimiter="\t")

final=[]

for one in df[0]:
    new=one.split(':')
    final.append(new)
    
f1=pd.DataFrame(final)
f1=f1.fillna(value=" ")
f2=f1[2]
f2_list=list(f2)
ham_words = ' '.join(f2_list)

ham_wc = WordCloud(width = 512,height = 512).generate(ham_words)
plt.figure(figsize = (10, 8), facecolor = 'k')
plt.imshow(ham_wc)
plt.axis('off')
plt.tight_layout(pad = 0)
plt.show()


