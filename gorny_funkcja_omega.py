# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 22:18:47 2019

@author: Marta
"""

import numpy as np
from cena import *
from Omega import *

def Theta_omega(b,n,S0,K,r,sigma,ziarno):
    rm.seed(ziarno)
    w = np.zeros(n+1) 
    v = np.zeros([b,n+1])
    omega = np.zeros(b)
    
    v[0,0] = S0
    
    for j in range(1,n+1):
        v[0,j] = cena(v[0,j-1],r,sigma,n)
    
    j == n
    
    while(j > -1): #bo w pythonie 0 też wchodzi, a ja biorę s0 jako początek
        if (j == n and w[j] < b-1):
            #w[j] = int(w[j])
            omega[int(w[j])] = Omega(v[int(w[j]),j])
            v[int(w[j]),j] = max(0,K-v[int(w[j]),j]) #wartosc estymatora Theta! dla momentu wygasniecia
            v[int(w[j])+1,j] = cena(v[int(w[j-1]),j-1],r,sigma,n)
            w[j] = w[j]+1
        elif(j == n and w[j] == b-1):
            omega[int(w[j])] = Omega(v[int(w[j]),j])
            v[int(w[j]),j] = max(0,K-v[int(w[j]),j])
            w[j]=-1
            j = j-1
            #print(omega)
    
        elif(j < n and w[j] < b-1):
            suma = 0
            for k in range(b):
                suma = suma + v[k,j+1]*exp(-omega[k]/n)
            v[int(w[j]),j] =  max(max(0,K-v[int(w[j]),j]), suma/b) #wartosc estymatora Theta dla t_i, i !=n
            if(j>0):
                v[int(w[j]+1),j] = cena(v[int(w[j-1]),j-1],r,sigma,n)
                w[j] = w[j]+1
                v[0,j+1] = cena(v[int(w[j]),j],r,sigma,n)
                w[j+1] = 0
                for i in range(j+2,n+1):
                    v[0,i] = cena(v[0,i-1],r,sigma,n)
                    w[i] = 0
                j = n
            else:
                j = -1
        elif(j < n and w[j] == b-1):
            suma = 0
            for k in range(b):
                suma = suma + v[k,j+1]*exp(-omega[k]/n)
            v[int(w[j]),j] =  max(max(0,K-v[int(w[j]),j]), suma/b) #wartosc estymatora Theta dla t_i, i !=n
            w[j]=0
            j = j-1
    return(v[0,0])