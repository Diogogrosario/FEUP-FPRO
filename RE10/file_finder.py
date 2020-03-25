#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 09:37:03 2018

@author: diogo
"""


def file_finder(dirs, file_name):
    if dirs == file_name:
        return file_name
    for i in dirs[1:]:
        if file_finder(i,file_name) != None:
            return dirs[0] + "/" + file_finder(i,file_name) 
