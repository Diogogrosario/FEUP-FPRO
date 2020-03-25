#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 11:53:49 2018

@author: diogo
"""

def parse(filename):
    result=""
    with open(filename,'r') as fn:
        linhas = fn.readlines()
        for i in range(len(linhas)):
            while " " in linhas[i]:
                linhas[i]=linhas[i].strip(" ")
            linhas[i]=linhas[i].strip("\n")
        for linha in linhas:
            if linha =='(':
                result+='('
            else:
                result+=linha+','
        result='('+result+')'
    return eval(result)