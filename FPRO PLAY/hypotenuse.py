#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 18:12:53 2018

@author: diogo
"""
import math

def hypotenuse(n):
    hypo = float(math.sqrt(n**2+n**2))
    return round(hypo,2)