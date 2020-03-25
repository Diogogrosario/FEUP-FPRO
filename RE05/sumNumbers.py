#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 21:34:31 2018

@author: diogo
"""

def sum_numbers(n):
    """
    returns the sum of all positive integers up to and including n
    """
    sum=0
    for i in range(n+1):
        sum = sum + i
    return sum