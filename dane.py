# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 19:57:56 2019

@author: Marta
"""
from dolny_funkcja_omega import *
from gorny_funkcja_omega import *
import pandas as pd

df = pd.read_csv("test.csv",names = ["b","Theta","Phi","estimated price"], header = 0,  sep = ";")

N = 100 #ilosc symulowanych drzew
K = 145
n = 3
S0 = 168.33
r = 0.0225
sigma = 0.155 

for i in range(np.shape(df)[0]):
    b = df.iloc[i,0]
    gorny = 0
    dolny = 0

    for j in range(N):
        gorny += Theta_omega(b,n,S0,K,r,sigma,j+10)
        dolny += Phi_omega(b,n,S0,K,r,sigma,j+10)
    
    gorny = gorny/N
    dolny = dolny/N
    df.iloc[i,1] = gorny
    df.iloc[i,2] = dolny
    df.iloc[i,3] = (gorny+dolny)/2
    
print(df)
df.to_csv("policzony_b_fb.csv", sep = ";", index = False)