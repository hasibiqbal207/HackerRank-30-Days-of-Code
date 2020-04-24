# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 19:42:00 2020

@author: Hasib Iqbal
"""
n = int(input())
dict = {}

for i in range(n):
    try:
        key,value = input().split()
    except:
        continue
    dict[key] = value

try:
    k = input()
    while k != "":
        if k in dict:
            print(k+'='+dict[k])
        else:
            print("Not found")
        k = input()
except:
    None