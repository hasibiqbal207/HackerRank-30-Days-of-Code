# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 13:21:46 2020

@author: Hasib Iqbal
"""

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
        
    sum = 0
    ind = True


    for i in range(4):
        for j in range(4):
            sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2] + arr[i+1][j+1]  
            if ind:
                max_value = sum
                ind = False
                continue
            

            if max_value < sum:
                max_value = sum
    
    print(max_value)