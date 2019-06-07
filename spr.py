# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 21:41:01 2019

@author: Marta
"""

from dolny_funkcja import *
from gorny_funkcja import *
#from gorny_funkcja_omega import *
#from dolny_funkcja_omega import *

N = 100 #ilosc symulowanych drzew

gorny = 0
dolny = 0
#gorny_omega = 0
#dolny_omega = 0

b = 100
n = 3
S0 = 100
K = 100
r = 0.05
sigma = 0.2 

for i in range(N):
    gorny += Theta(b,n,S0,K,r,sigma,i+100)
    dolny += Phi(b,n,S0,K,r,sigma,i+100)
    #gorny_omega += Theta_omega(b,n,S0,K,r,sigma,i+123)
    #dolny_omega += Phi_omega(b,n,S0,K,r,sigma,i+123)
    
gorny = gorny/N
dolny = dolny/N
#gorny_omega = gorny_omega/N
#dolny_omega = dolny_omega/N

print("Estymatory dla amerykańskiej odp górny i dolny to: \n ",gorny, "i",dolny)
#print("a dla omega clock \n", gorny_omega, "i", dolny_omega)
print("Estymowane ceny to odpowiednio: \n waniliowa:", (gorny+dolny)/2)#, "\n omega clock: ", (gorny_omega+dolny_omega)/2)