# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 10:51:33 2020

@author: Hasib Iqbal
"""

class Difference:
    def __init__(self, a):
        self.__elements = a
        
    maximumDifference = 0

    # Add your code here
    def computeDifference(self):
        ln = len(a)
        
        for i in range(ln-1):
            for j in range(ln):
                diff = abs(a[i]-a[j])
                if diff > self.maximumDifference:
                    self.maximumDifference = diff
        

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)