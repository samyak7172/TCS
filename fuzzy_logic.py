#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 11:55:45 2020

@author: samyak
"""


## Fuzzy Logic
def fuzzy(weight):
    if weight==0:
        print("Time Estimated:0 minutes")
    elif weight in range(0,2001):
        print("Time Estimated:25 minutes")
    elif weight in range(2001,4001):
        print("Time Estimated:35 minutes")
    elif weight in range(4001,7001):
        print("Time Estimated:45 minutes")
    elif weight>7000:
        print("OVERLOADED")
    else:
        print("INVALID INPUT")

if __name__ =='__main__':
    weight = int(input())
    fuzzy(weight)
        
    