# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 17:16:07 2020

@author: Hasib Iqbal
"""

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost * (tip_percent/100)
    tax = meal_cost * (tax_percent/100)
    total = meal_cost + tip + tax
    return round(total)

    
    
if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    print(solve(meal_cost, tip_percent, tax_percent))
