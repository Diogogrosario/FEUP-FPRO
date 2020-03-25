#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 21:27:59 2018

@author: diogo
"""

s1=int(input("First side: "))
s2=int(input("Second side: "))
s3=int(input("Third side: "))
    
    
if s1 + s2 < s3 or s1 + s3 < s2 or s2 + s3 < s1:
    result="Not a triangle"
elif s1==s2 and s2==s3:
    result="Equilateral"
elif s1!=s2!=s3:
    result="Scalene"
else:
    result="Isosceles"
        
print(result)
