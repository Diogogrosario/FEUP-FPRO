#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 18:12:30 2018

@author: diogo
"""

def pattern_hunting(l1,l2,p):
	result = []
	for i in range(len(l1)):
		if p in l1[i]:
			result += [l2[i]]
		elif p in l2[i]:
			result += [l1[i]]
	result = sorted(result, reverse = True)
	return result