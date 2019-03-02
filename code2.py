#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 12:21:03 2018

@author: raja
"""


from nltk.tree import ParentedTree

def parser2path(textt):    
    
    def get_labels_from_lca(ptree, location):
        labels = []
        for i in range(0, len(location)):
            labels.append(ptree[location[:i]].label())
        return labels
    
    def findPath(ptree, text1):
        leaf_values = ptree.leaves()
        leaf_index1 = leaf_values.index(text1)
        
    
        location1 = ptree.leaf_treeposition(leaf_index1)
        
    
        labels1 = get_labels_from_lca(ptree, location1)
        #ignore the first element, because it will be counted in the second part of the path
        result = labels1[1:]
        #inverse, because we want to go from the node to least common ancestor
        
        return result
    
    """
    textt="(ROOT  (S    (NP (DT The) (JJ quick) (JJ brown) (NN fox)) \
        (VP (VBZ sucks)\
          (PP (IN at)\
            (S\
              (VP (VBG jumping)))))\
        (. .)))"
    
    """
    
    ptree = ParentedTree.fromstring(textt)
    
    leaf_values = ptree.leaves()
    k=[]
    for tt in leaf_values:
        k.append(findPath(ptree,tt))

    return k








