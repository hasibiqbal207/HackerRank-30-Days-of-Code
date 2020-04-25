# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 11:47:27 2020

@author: Hasib Iqbal
"""
class Calculator():
    def power(self, a, b):
            if a>=0 and b>=0:
                return pow(a,b)
            else:
                raise Exception("n and p should be non-negative")
   
myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e) 