#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 18:08:34 2018

@author: diogo
"""

def add_item(tup, idx, item):
	if idx == 0:
		tup = (item,) + tup[1:]
	elif idx == (len(tup)-1) or idx == -1:
		tup = tup[:len(tup)-1] + (item,)
	else:
		tup = tup[:idx] + (item,) + tup[idx:]
	return tup 