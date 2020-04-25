# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 13:11:20 2020

@author: Hasib Iqbal
"""

if __name__ == '__main__':
    n = int(input())

    a = bin(n).replace("0b","").split("0")
    a.sort(key=len,reverse=True)
    print(len(a[0]))