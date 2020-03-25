#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 18:02:37 2018

@author: diogo
"""

def discard_middle(s):
	if len(s) >= 4:
		s = s[:2] + s[len(s)-2:]
		return s
	else:
		return ""