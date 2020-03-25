#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 21:29:28 2018

@author: diogo
"""

def to_fahrenheit(t):
	return list(map((lambda x:round(x*1.8+32,2)),t))