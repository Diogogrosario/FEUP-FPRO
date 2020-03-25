#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 09:23:58 2019

@author: diogo
"""

def rec_exceptions(l):
    result = []
    for i in l:
        try:
            i()
        except Exception as ex:
            result.append(ex)
        else:
            result += rec_exceptions(i())
    return result

