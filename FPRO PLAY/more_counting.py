#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 18:10:53 2018

@author: diogo
"""

def count_elems(tup):
	result = ()
	for i in tup:
		if type(i) == tuple:
			result += (len(i),)
		elif type(i) == list:
			result += (len(i),)
		elif type(i) == int:
			i = str(i)
			result += (len(i),)
		elif type(i) == str:
			result += (len(i),)
		else:
			result += (1,)
	return result