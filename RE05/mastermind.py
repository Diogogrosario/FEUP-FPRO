#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 21:54:48 2018

@author: diogo
"""

def mastermind(g1, g2, g3, c1, c2, c3):
    
    if g1==c1:
        if g2==c2:
            if g3==c3:
                return 9
            elif g3==c1 or g3 == c2:
                return 7
            else:
                return 6
        elif g2 == c3 or g2 == c1:
            if g3 == c3:
                return 7
            elif g3 == c1 or g3 == c2:
                return 5
            else:
                return 4
        else:
            if g3 == c3:
                return 6
            elif g3 == c1 or g3 == c2:
                return 4
            else:
                return 3
    elif g1 == c2 or g1 == c3:
        if g2==c2:
            if g3==c3:
                return 7
            elif g3==c1 or g3 == c2:
                return 5
            else:
                return 4
        elif g2 == c3 or g2 == c1:
            if g3 == c3:
                return 5
            elif g3 == c1 or g3 == c2:
                return 3
            else:
                return 2
        else:
            if g3 == c3:
                return 4
            elif g3 == c1 or g3 == c2:
                return 2
            else:
                return 1
    else:
        if g2==c2:
            if g3==c3:
                return 6
            elif g3==c1 or g3 == c2:
                return 4
            else:
                return 3
        elif g2 == c3 or g2 == c1:
            if g3 == c3:
                return 4
            elif g3 == c1 or g3 == c2:
                return 2
            else:
                return 1
        else:
            if g3 == c3:
                return 3
            elif g3 == c1 or g3 == c2:
                return 1
            else:
                return 0