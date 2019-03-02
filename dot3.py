#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 22:04:45 2018

@author: raja
"""

from nltk.tree import ParentedTree
import numpy as np

#text123="(ROO69 (76 (52 (52 (66 69he) (59 system)) (11 (63 as) (76 (48 (32 described) (50 (63 above)))))) (48 (30 has) (52 (52 (3872 its) (43 greatest) (59 application)) (50 (63 in) (52 (52 (66 an)) (48 (32 arrayed) (52 (52 (59 configuration)) (50 (63 of) (52 (59 antenna) (42 elements))))))))) (75 75)))"
    
def path2beforeAfterLength(textt):
    text123=textt
    def get_lca_length(location1, location2):
        i = 0
        while i < len(location1) and i < len(location2) and location1[i] == location2[i]:
            i+=1
        return i
    
    def get_labels_from_lca(ptree, lca_len, location):
        labels = []
        for i in range(lca_len, len(location)):
            labels.append(ptree[location[:i]].label())
        return labels
    
    def findPath(ptree, text1, text2):
        leaf_values = ptree.leaves()
        leaf_index1 = leaf_values.index(text1)
        leaf_index2 = leaf_values.index(text2)
    
        location1 = ptree.leaf_treeposition(leaf_index1)
        location2 = ptree.leaf_treeposition(leaf_index2)
    
        #find length of least common ancestor (lca)
        lca_len = get_lca_length(location1, location2)
    
        #find path from the node1 to lca
    
        labels1 = get_labels_from_lca(ptree, lca_len, location1)
        #ignore the first element, because it will be counted in the second part of the path
        result = labels1[1:]
        #inverse, because we want to go from the node to least common ancestor
        result = result[::-1]
    
        #add path from lca to node2
        result = result + get_labels_from_lca(ptree, lca_len, location2)
        return result
    
    ptree = ParentedTree.fromstring(text123)
    leaff=ptree.leaves()
    pre_sent=np.zeros((len(ptree.leaves())))
    aft_sent=np.zeros((len(ptree.leaves())))
    prime=np.array([2,3,5,7,11,13,17,19,23,29,31,37,41,
                            43,47,53,59,61,67,71,73,79,83,89,97,101, 103, 
                            107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 
                            167, 173, 179, 181, 191, 193, 197])
    
    count=len(leaff)
    if count>29:
        count=29
        
    for k in range(0,count):
        if k!=0:
            ppath=np.array(findPath(ptree,leaff[k],leaff[k-1]))
            ppath=ppath.astype(int)
            pre_sent[k]=np.dot(ppath,prime[0:np.size(ppath)])
            
        if k!=len(leaff)-1:
            ppath2=np.array(findPath(ptree,leaff[k],leaff[k+1]))
            ppath2=ppath2.astype(int)
            size2=np.size(ppath2)
            aft_sent[k]=np.dot(ppath2,prime[0:size2])
            
            pre_sent1=pre_sent[0:30]
            
            aft_sent1=aft_sent[0:30]
            
    return pre_sent1 , aft_sent1