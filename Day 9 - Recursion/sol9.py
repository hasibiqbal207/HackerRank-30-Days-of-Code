# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 22:51:12 2020

@author: Hasib Iqbal
"""

def factorial(n):
    if n==1:
        return 1

    return factorial(n-1)*n

if __name__ == '__main__':
    n = int(input())

    result = factorial(n)

    print(result)