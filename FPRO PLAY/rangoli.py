# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 22:20:30 2018

@author: Diogo
"""



import string

def rangoli(N):
    alphabet = string.ascii_lowercase[:N]
    result = ""
    for x in range(N):
        line = ""
        for y in range(N-1, N-x-2, -1):
            line += alphabet[y] + "-"
        line = line[:-1] + line[-3::-1]
        sem_tracos = line
        line = line.zfill(2*N -1 + 2*x)
        line = line + line[:2*N -1 + 2*x -len(sem_tracos)]
        line = line.replace("0", "-")
        result += line + "\n"
    result = result[:-1].split("\n")
    result_2 = result[::-1]
    result = result + result_2[1:]
    result = "\n".join(result)
    return result

print(rangoli(26))
        
        
        