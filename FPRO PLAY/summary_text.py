#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 18:11:08 2018

@author: diogo
"""

def summary(text):
	count = 0
	words = text.split()
	e_count = 0
	for i in words:
		count += 1
	for letters in words:
		if "e" in letters or "E" in letters:
			e_count += 1
	return (count, e_count)