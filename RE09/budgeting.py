#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 09:57:25 2018

@author: diogo
"""

def budgeting(budget, products, wishlist):
    final={}
    final2 = {}
    d1 = {}
    products=sorted(products.items(),key=lambda x:x[1],reverse=True)
    
    for i in products:
        if i not in d1:
            d1[i[0]]=i[1]
    for i in d1:
        if i in wishlist:
            for k in range(wishlist[i]):
                budget -= d1[i]
                if budget>=0 and i not in final:
                    final[i]=1
                elif budget<0:
                    budget += d1[i]
                elif budget>=0 and i in final:
                    final[i]+=1
    for item in wishlist:
        if item not in final:
            pass
        else:
            final2[item]=final[item]
        
    return final2
print(budgeting(1000, {'ps4': 350, 'smartphone': 400, 'jacket': 40,'pc': 600, 'glasses': 75}, {'ps4': 1, 'smartphone': 1, 'pc': 1}))