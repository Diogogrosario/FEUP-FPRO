#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 10:18:19 2018

@author: diogo
"""

def soup(matrix, word):
    for index,i in enumerate(matrix):
        for inde,j in enumerate(i):
            if j == word[0]:
                if check_soup(matrix,word,index,inde):
                    return "{}{}".format(chr(ord("A")+index), inde+1) 
                    

def check_soup(matrix,word,line,column):
    if word == "":
        return True
    else:
        for k in range(line-1,line+2):
            for l in range(column-1,column+2):
                if k>=0 and l>=0 and k<len(matrix) and l<len(matrix[0]) and word[0] == matrix[k][l]:
                    return check_soup(matrix,word[1:],k,l)
mx = (('X', 'A', 'B', 'N', 'T', 'O'),
('Y', 'T', 'N', 'R', 'I', 'T'),
('U', 'P', 'O', 'M', 'D', 'S'),
('I', 'O', 'H', 'U', 'O', 'O'),
('R', 'T', 'E', 'L', 'Q', 'X'),
('I', 'W', 'J', 'K', 'P', 'Z'))

print(soup(mx, "HOTEL"))
        
    