# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 21:33:21 2019

@author: Marta
"""
from math import exp
import random as rm

def cena(x,r,sigma,n): #cena obliczająca następną cenę z poprzedniej danej x
    S = x*exp((r-sigma**2/2)/n +sigma/n**(1/2)*rm.normalvariate(0,1))
    return(S)