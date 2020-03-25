#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 14:50:53 2018

@author: diogo
"""

def anagrams(alist):
    anagram_list = []
    novo = []
    result = []
    for s in alist:
        s = s.replace(" ", "")
        s = s.lower()
        novo += ["".join(sorted(s))]
    for n in range(len(novo)):
        anagram_group = [alist[n]]
        for x in range(len(novo)):
            if n != x:
                if (novo[n] == novo[x]):
                    anagram_group += [alist[x]]
                    anagram_group = sorted(anagram_group)
        anagram_list += [anagram_group]
    for i in anagram_list:
        if i not in result:
            result += [i]
    result.sort(key=lambda x:x[0].lower())
    return result

print(anagrams(['sentence', 'lives', 'ten scene', 'bat', 'Elvis', 'CE sennet']))