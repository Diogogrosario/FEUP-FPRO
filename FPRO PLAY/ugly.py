#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 18:02:20 2018

@author: diogo
"""

def ugly(n):
	while n != 1:
		if n % 2 == 0:
			n = n/2
		elif n % 3 == 0:
			n= n/3
		elif n % 5 == 0:
			n = n/5
		else:
			return False
	return True