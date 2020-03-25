#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 00:11:40 2018

@author: diogo
"""
def getPosition():
    if(word_list[0] + " "+ word_list[1]) == sentence:
        result = "0 1"
        return result
    elif(word_list[0] + " "+ word_list[2]) == sentence:
        result = "0 2"
        return result
    elif(word_list[1] + " "+ word_list[0]) == sentence:
        result = "1 0"
        return result   
    elif(word_list[1] + " "+ word_list[2]) == sentence:
        result = "1 2"
        return result
    elif(word_list[2] + " "+ word_list[0]) == sentence:
        result = "2 0"
        return result
    elif(word_list[2] + " "+ word_list[1]) == sentence:
        result = "2 1"
    return result