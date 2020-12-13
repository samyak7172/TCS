#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 13:44:49 2020

@author: samyak
"""


##Caesar cipher
def caesar_cipher(move,code):
    for elements in range(0,len(code)):
        char = ord(code[elements])
        if char == 32:
            print(" ",end="")
        else:
            char += move
            char =chr(char)
            print(char,end="")
        

if __name__ == "__main__":
    caesar_cipher(1,"z")
 




