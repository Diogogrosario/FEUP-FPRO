#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 08:48:30 2018

@author: diogo
"""

def count(word, phrase):
    count = 0
    phrase = phrase.lower()
    word = word.lower()
    phrase = phrase.split()
    for i in phrase:
        if word == i: 
            count += 1
    return count

print(count("shells",'Sally sells sea shells by the sea shore. But if Sally sells sea shells by the sea shore then where are the sea shells Sally sells?'))