#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 09:12:18 2018

@author: diogo
"""
import functools as ft

def reduce_map_filter(args):
    if isinstance(args[2],tuple):
        return reduce_map_filter((args[0],args[1],reduce_map_filter(args[2])))
    else:
        if args[0] == "reduce":
            return int(ft.reduce(args[1],args[2]))
        elif args[0] == "map":
            return list(map(args[1],args[2]))
        elif args[0] == "filter":
            return list(filter(args[1],args[2]))
        
            
        
        
    
