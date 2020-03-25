#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 18:05:21 2018

@author: diogo
"""

def palindrome_index(s):
	for i in range(len(s)):
		test = s[:i] + s[i+1:]
		if test == test[::-1]:
			return i
		elif s == s[::-1]:
			return -1
		else:
			score = -1
	return score
