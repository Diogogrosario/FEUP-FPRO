#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 18:15:46 2018

@author: diogo
"""

def alarm(hour,minutes):
	if minutes+51 > 60:
		alarm_m = (minutes+51)%60
		hour += 1
	else:
		alarm_m = (minutes+51)%60
	alarm_h = (hour+6)%24
	return "{0}:{1}".format(str(alarm_h).zfill(2),str(alarm_m).zfill(2))

