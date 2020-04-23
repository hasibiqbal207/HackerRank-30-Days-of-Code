# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 19:41:15 2020

@author: Hasib Iqbal
"""

arr = []
n = int(input())

arr = [int(x) for x in input().rstrip().split()]

#==============================================================================
# for j in reversed(range(n)):
#     print(arr[j], end=' ')
# 
#==============================================================================
for j in range(n-1,-1,-1):
    print(arr[j], end=' ')
