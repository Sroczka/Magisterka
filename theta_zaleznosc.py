# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 17:11:53 2019

@author: Marta
"""

import sys

from gorny_funkcja_omega3d import *
from zmienne import *

import pandas as pd

nazwa_csv = sys.argv[1]
nazwa_csv +=".csv" 

df = pd.DataFrame(columns = kolumny)
df = df.to_csv(nazwa_csv, sep = ";", index = False)
for i in range(np.shape(r1)[0]):
    linia_danych=list()
    #df = pd.DataFrame(columns = kolumny)
    for j in range(np.shape(r2)[0]):
        gorny = 0
        dolny = 0
        for k in range(N):
            gorny += Theta_omega3d(b,n,S0,K,r,sigma,r1[i],r2[j],prog_zmiany,3*k)
        Z[i,j] = gorny/N
        linia_danych.append(Z[i,j])
    #df = df.append(linia_danych,ignore_index=True)
    with open(nazwa_csv, 'a') as file:
        file.writelines(str(linia_danych)[1:-1].replace(',',';')+"\n")
        file.close()
        
print("koniec")