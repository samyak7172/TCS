#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 14:31:07 2020

@author: samyak
"""


def cost_func(interior,exterior):
    if interior and exterior == 0:
        print("Don't want to paint the wall")
    else:    
        list_int = []
        list_ext = []
        for i in range(0,interior):
            list_int.append(float(input())*18)
        for j in range(0,exterior):
            list_ext.append(float(input())*12)
        result = sum(list_int) + sum(list_ext)
    return result

if __name__ == "__main__":
    result = cost_func(int(input("No. of Interior walls \n")),int(input("No. of exteriror walls \n")))
    print("Total estimated Cost :",result)