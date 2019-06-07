# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 21:35:24 2019

@author: Marta
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 11:39:12 2019

@author: Marta
"""

import numpy as np
from cena import *

def Phi(b,n,S0,K,r,sigma,ziarno):
    rm.seed(ziarno)
    w = np.zeros(n+1)
    v = np.zeros([b,n+1])
    
    v[0,0] = S0
    
    #rm.seed(1345)
    for j in range(1,n+1):
        v[0,j] = cena(v[0,j-1],r,sigma,n)
    
    j == n
    
    while(j > -1): #bo w pythonie 0 też wchodzi, a ja biorę s0 jako początek
        if (j == n and w[j] < b-1):
            #w[j] = int(w[j])
            v[int(w[j]),j] = max(0,K-v[int(w[j]),j]) #wartosc estymatora Phi! dla momentu wygasniecia
            v[int(w[j])+1,j] = cena(v[int(w[j-1]),j-1],r,sigma,n)
            w[j] = w[j]+1
            #print("tak")
        elif(j == n and w[j] == b-1):
            v[int(w[j]),j] = max(0,K-v[int(w[j]),j])
            w[j]=-1
            j = j-1
            #print("nie")
    
        elif(j < n and w[j] < b-1):
            #print("OOOOOooooo")
            h = max(0,K-v[int(w[j]),j]) #wczesniejsza funkcja wyplaty
            eta = np.zeros(b)
            for k in range(b):
                suma = (sum(v[:,j+1]) - v[k,j+1])/(b-1)
                if(suma*exp(-r/n)>h):
                    eta[k] = v[k,j+1] * exp(-r/n)
                else:
                    eta[k] = h
            v[int(w[j]),j] = sum(eta)/b
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
            h = max(0,K-v[int(w[j]),j]) #wczesniejsza funkcja wyplaty
            eta = np.zeros(b)
            for k in range(b):
                suma = (sum(v[:,j+1]) - v[k,j+1])/(b-1)
                if(suma*exp(-r/n)>h):
                    eta[k] = v[k,j+1] * exp(-r/n)
                else:
                    eta[k] = h
            v[int(w[j]),j] = sum(eta)/b
            w[j]=0
            j = j-1
            #print("cos")
    return(v[0,0])