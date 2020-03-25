#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 09:18:07 2018

@author: diogo
"""

def cut(filename, delimiter, field):
    result = []
    with open(filename, "r") as file:
        file = file.read()
        for i in file.split("\n"):
            i = i.split(delimiter)
            if type(field) == list:
                use = []
                for j in field:
                    if len(i) >= j:
                        use.append(i[j-1])
                result.append(delimiter.join(use))
            else:
                if len(i)>= field:
                    result.append(i[field-1])
    return "\n".join(result)
