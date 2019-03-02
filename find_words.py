#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 04:15:27 2018

@author: raja
"""

#(?<=% of )(.*)(?= at )

import re


s = 'Part 1. Part 2. 3.6.5 |Anaconda, Inc.| (default, Apr 29 2018, 16:14:56) Part 3 then more text'
pattern=r'Anaconda(.*?)2018'
re.search(pattern, s).group(1)
print(s)
print('checking  check the king maker')

