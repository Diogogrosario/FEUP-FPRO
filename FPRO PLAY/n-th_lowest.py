#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 18:11:32 2018

@author: diogo
"""

def nth_lowest(lnum,n):
	lnum.sort()
	return lnum[n-1]
	