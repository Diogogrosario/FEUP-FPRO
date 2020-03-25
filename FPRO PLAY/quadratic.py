#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 18:01:30 2018

@author: diogo
"""

def solver(a,b,c):
	root = (b*b)-(4*a*c)
	if root < 0 or a == 0:
		result = []
	elif root == 0:
		sol = -b/(2*a)
		result = [sol]
	elif root > 0:
		sol1 = (-b+(root**0.5))/(2*a)
		sol2 = (-b-(root**0.5))/(2*a)
		result = [sol1,sol2]
		result = sorted(result)
	return result
