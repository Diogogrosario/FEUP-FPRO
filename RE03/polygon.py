#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 09:17:57 2018

@author: diogo
"""

import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")

John=turtle.Turtle()
John.color("red")
John.pensize(3)

for i in range(4):
    John.forward(100)
    John.left(90)
    
for i in range(3):
    John.forward(100)
    John.left(120)
    
for i in range(6):
    John.forward(100)
    John.left(60)
    
for i in range(8):
    John.forward(100)
    John.left(45)

wn.exitonclick()    
wn.mainloop()