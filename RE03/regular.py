#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 08:42:13 2018

@author: diogo
"""

import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Random Polygon")

sides = input("Number of sides: ")
side_lenght = input("Side lenght: ")
border_color = input("Color: ")
fill_color = input("Color: ")

John=turtle.Turtle()
John.color(border_color)
John.pensize(3)
John.fillcolor(fill_color)
John.begin_fill()

for i in range(int(sides)):
    John.forward(int(side_lenght))
    John.left(360/int(sides))
    
John.end_fill()
    
wn.exitonclick()    
wn.mainloop()