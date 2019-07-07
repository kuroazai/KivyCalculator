# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 21:33:05 2019

@author: KuroAzai
"""



def Addition(a,b):
    #check if it's an int or decimal 
    if "." in str(a) or "." in str(b):
        return float(a) + float(b)
    else:
        return int(a) + int(b)
    

def Subtraction(a,b):
    #check if it's an int or decimal 
    if "." in str(a) or "." in str(b):
        return float(a) - float(b)
    else:
        return int(a) - int(b)


def Division(a,b):
    #check if it's an int or decimal 
    if "." in str(a) or "." in str(b):
        return float(a) / float(b)
    else:
        return int(a) / int(b)


def Multiplication(a,b):
    #check if it's an int or decimal 
    if "." in str(a) or "." in str(b):
        return float(a) * float(b)
    else:
        return int(a) * int(b)


