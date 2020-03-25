#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 18:02:54 2018

@author: diogo
"""

def longest(s):
	s= s.split()
	final = 0
	for i in range(len(s)):
		if len(s[i]) > final:
			final = len(s[i])
	return final