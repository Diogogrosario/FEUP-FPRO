#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 18:09:50 2018

@author: diogo
"""

import random 
from math import sqrt
from statistics import stdev,mean

def in_circle(point):    #Definir pontos internos no círculo através da fórmula
    x=random.random()
    y=random.random()
    return sqrt(x**2 + y**2) <= 1.0

def shoot_needle(n):     #função que atira as setas para n setas
    circle_needles = 0
    square_lenght = 2
    square_area = square_lenght**2
    for i in range(n):
        point = [random.uniform(-1.0,1.0),random.uniform(-1.0,1.0)] 
        if in_circle(point):
            circle_needles += 1                 #pontos dentro do círculo
    return (square_area)*circle_needles/n       #retorna o valor da área do círculo = pi

def estimate(n,total_estimates):      #função que calcula estimativa para 100 simluações de 1000 setas
    p = []                            #lista de valores das 100 estimativas
    for i in range(total_estimates):
        pi = shoot_needle(n)          
        p.insert(0,pi)            #adiciona os valores de pi à lista p das estimativas
    var_pi = stdev(p)             #standard deviation
    pi_estimate = mean(p)         #calculo da média
    return pi_estimate, var_pi    #retorna o valor da média das estimativas e da standard deviation
    
def final_estimation(deviation, total_estimates):  #função para cĺculo da estimativa final
    n=1000                                         #nº setas atiradas
    var_pi = deviation                             
    while var_pi >= deviation :                    #para estimativas superiores ao desvio pretendido
        pi_estimate, var_pi = estimate(n, total_estimates) #os valores retornoados pela função estimate são alterados, nº de setas*2
        n *= 2
    return pi_estimate,n, var_pi             #retorna estimativa do pi

print(final_estimation(0.005,100))           #cálculo final para desvio de 0.005 e 100 estimativas



