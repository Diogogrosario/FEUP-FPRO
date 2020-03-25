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
John.color("blue")
John.shape("turtle")
John.stamp()
John.pensize(3)

for i in range(12):
    John.penup()
    John.forward(80)
    John.pendown()
    John.forward(10)
    John.penup()
    John.forward(10)
    John.stamp()
    John.backward(100)
    John.left(30)
    
    
wn.exitonclick()    
wn.mainloop()