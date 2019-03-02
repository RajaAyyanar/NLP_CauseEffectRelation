#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 12:15:16 2018

@author: raja
"""

#java -mx1g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9010 -timeout 15000


from nltk.parse.corenlp import CoreNLPParser
parser = CoreNLPParser(url='http://localhost:9010')
#parsed = next(     parser.raw_parse('The quick brown dogs and tigers may suck at jumping.')
#     ).pretty_print()

#text =  "The runner scored from second on a base hit"

#text= "Literary criticism is the study of literature by means of a microscopic knowledge of the language in which a book is written, of its growth from various roots, of its stages of development and the factors influencing them, of its condition in the period of this particular composition, of the writer's idiosyncrasies of thought and style in his ripening periods, of the general history and literature of his race, and of the special characteristics of his age and of his contemporary writers"
text= "good boy Ajil is going to marry sanju at kerala"

parse123 = next(parser.parse_text(text))

#Flattenning the tree
parse_string = ' '.join(str(parse123).split()) 
