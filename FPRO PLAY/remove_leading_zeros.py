#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 18:03:47 2018

@author: diogo
"""

def remove_leading(ip):
	ip = ip.replace(".", " ")
	ip = ip.split()
	final = ""
	for number in ip:
		if len(number)>2 and number[0]=="0" and number[1]=="0":
			number = number[2] + "."
			final += number
		elif len(number)>1 and number[0]=="0":
			number = number[1:] + "."
			final += number
		else:
			final += number + "."
	final = final[:-1]
	return final
