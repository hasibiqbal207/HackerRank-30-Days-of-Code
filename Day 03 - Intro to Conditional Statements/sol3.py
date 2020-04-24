# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 17:25:59 2020

@author: Hasib Iqbal
"""

if __name__ == '__main__':
    N = int(input())
    
    if N % 2 == 1 or N in range(6,21):
        print('Weird')
#    elif N > 20 or N in range(2,6):
    else:
        print('Not Weird')