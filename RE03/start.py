#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 22:23:06 2018

@author: diogo
"""

import turtle
wn = turtle.Screen()
wn.bgcolor("blue")

John=turtle.Turtle()
John.color("white")
John.shape("circle")
John.pensize(2)
John.stamp

for i in range(8):
    John.forward(150)
    John.stamp()
    John.backward(150)
    John.left(45)

    
wn.exitonclick()    
wn.mainloop()   