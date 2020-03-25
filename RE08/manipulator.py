#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 09:05:09 2018

@author: diogo
"""

def manipulator(l,cmds):
    final = ""
    for i in cmds:
        com = i.split()
        if com[0] == "insert":
            l.insert(int(com[1]),int(com[2]))
        elif com[0] == "print":
            final += str(l) + " "
        elif com[0] == "remove":
            l.remove(int(com[1]))
        elif com[0] == "append":
            l.append(int(com[1]))
        elif com[0] == "sort":
            l.sort()
        elif com[0] == "pop":
            l.pop(-1)
        elif com[0] == "reverse":
            l = l[::-1]
    final = final [:-1]
    return final

