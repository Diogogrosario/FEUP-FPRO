#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 08:50:49 2018

@author: diogo
"""
result = 0
def calculator(expr):
    if type(expr) == int:
        return expr
    valor1 = expr[0]
    valor2 = expr[2]
    if type(expr[0]) == tuple:
        valor1 = calculator(expr[0])
    if type(expr[2]) == tuple:
        valor2 = calculator(expr[2])
    if expr[1] == "+":
            result = valor1+valor2
    elif expr[1] == "*":
            result = valor1*valor2
    elif expr[1] == "-":
            result = valor1-valor2
    return result
print(calculator(10))