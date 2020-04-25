# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 23:22:49 2020

@author: Hasib Iqbal
"""

actual = [int(x) for x in input().rstrip().split()]
due = [int(x) for x in input().rstrip().split()]

year = actual[2] - due[2]
month = actual[1] - due[1]
day = actual[0] - due[0]


if year<0 or (year == 0 and month < 0 and day <= 0):
    print(0)
elif year>0:
    print(10000)
elif month>0:
    print(500*month)
elif day>0:
    print(day*15)