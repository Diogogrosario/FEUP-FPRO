#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 09:31:09 2018

@author: diogo
"""

def longest_word(url):
    import urllib.request
    response = urllib.request.urlopen(url)
    html = response.read().decode()
    content1 = urllib.request.urlopen("https://raw.githubusercontent.com/fpro-admin/recitas/master/words")
    content = content1.read().decode()
    words_url=set(html.split())
    words_dict=set(content.split())
    words=words_url.intersection(words_dict)
    max_len=len(max(words,key=lambda x:len(x)))
    word=[w for w in words if len(w)==max_len]
    return sorted(word)[0]