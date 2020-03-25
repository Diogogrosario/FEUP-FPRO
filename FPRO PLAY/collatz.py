#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 18:02:15 2018

@author: diogo
"""

def collatz(n):
	result = str(n) + ","
	while n != 1:
		if n % 2 == 0:
			n = n/2
			result += str(int(n)) + ","
		else:
			n = n*3+1	
			result += str(int(n)) + ","
	result = result[:-1]
	return result

print(collatz(174724214224321244224))