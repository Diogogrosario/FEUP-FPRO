#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 18:09:47 2018

@author: diogo
"""

def count_until(tup):
	found = -1
	count = -1
	for i in tup:
		count += 1
		if type(i) == tuple:
			found = 0
			break
	if found == -1:
		return found
	else:
		return count
	