# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 11:40:13 2020

@author: Hasib Iqbal
"""

S = input().strip()

try:
    x = int(S)
    print(x)
except:
    print("Bad String")