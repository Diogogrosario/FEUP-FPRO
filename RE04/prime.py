    #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 21:29:48 2018

@author: diogo
"""

result = "Not yet implemented"
    
    #### MY CODE STARTS HERE ############################
    
n = int(input("Write ur number: "))

for i in range(2,n):
    if n % i == 0: 
        result = False
        break
    else:
        result = True
print(result)

