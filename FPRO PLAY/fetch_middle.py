#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 18:12:08 2018

@author: diogo
"""

def fetch_middle(lists):
	result = []
	number = 0
	for l in lists:
		if len(l) % 2 != 0:
			index = (len(l)-1)/2
			result += [l[int(index)]]
		else:
			number = (int(l[int(len(l)/2)]) + int(l[int(len(l)/2-1)]))/2
			result += [number]
	return result