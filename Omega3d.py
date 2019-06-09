# -*- coding: utf-8 -*-
"""
Created on Tue May 28 17:30:58 2019

"Funkja dyskonta"

@author: Marta
"""

def Omega3d(S,prog_zmiany,r1,r2):
    if(S>prog_zmiany):
        return r2
    else:
        return r1