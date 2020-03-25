#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 18:01:59 2018

@author: diogo
"""

from math import factorial

def pascal(n):
	result = ""
	for i in range (n):
		for r in range(i+1):
			result += " " + str(int(factorial(i)/(factorial(r)*factorial((i-r))))) 
		result += "\n"
	return result