#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 08:51:11 2018

@author: diogo
"""

def roman_to_integer(astring):
    valores = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
    integer = 0
    valor_sub = 0
    for index,i in enumerate(astring):
        if index<len(astring)-1 and valores[i]>=valores[astring[index+1]]:
            integer += valores[i]-valor_sub
            valor_sub=0
        elif index<len(astring)-1 and valores[i]<valores[astring[index+1]]:
            valor_sub = valores[i]
        if index==len(astring)-1:
            integer += valores[i]-valor_sub
            valor_sub=0
    return integer

print(roman_to_integer("LCV"))