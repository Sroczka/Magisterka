# -*- coding: utf-8 -*-
"""
Created on Tue May 28 17:30:58 2019

"Funkja dyskonta"

@author: Marta
"""

r1 = 0.05
r2 = 0.1

def Omega(S):
    r=0
    if(S>95):
        r = r2
    else:
        r = r1
    return r
