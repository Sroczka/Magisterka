'''
======================
3D surface (color map)
======================

Demonstrates plotting a 3D surface colored with the coolwarm color map.
The surface is made opaque by using antialiased=False.

Also demonstrates using the LinearLocator and custom formatting for the
z axis tick labels.
'''
import sys
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

from gorny_funkcja_omega3d import *
from dolny_funkcja_omega3d import *

import pandas as pd

b = 3
n = 2
K = 195
S0 = 190.15
r = 0.025
sigma = 0.155

prog_zmiany = 180

nazwa_csv = sys.argv[1]
nazwa_csv +=".csv" 

N = 1
# Make data.
r1 = np.linspace(0,0.0225, 100)#arange(0, 0.025, 0.001)
r2 = np.linspace(0.0225, 0.045, 100)#arange(0.025, 0.045, 0.001)
X = np.copy(r1)
Y = np.copy(r2)
X, Y = np.meshgrid(X, Y)

Z = np.zeros([np.shape(r1)[0],np.shape(r2)[0]])
kolumny = list()
for i in range(np.shape(r2)[0]):
        kolumny.append(r2[i])

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
            dolny += Phi_omega3d(b,n,S0,K,r,sigma,r1[i],r2[j],prog_zmiany,3*k)
        Z[i,j] = (gorny+dolny)/(2*N)
        linia_danych.append(Z[i,j])
    #df = df.append(linia_danych,ignore_index=True)
    with open(nazwa_csv, 'a') as file:
        file.writelines(str(linia_danych)[1:-1].replace(',',';')+"\n")
        file.close()

    #df = df.to_csv(nazwa_csv, sep = ";", index = False)
#Z = X**2#Phi_omega3d(b,n,S0,K,r,sigma,r1,r2,ziarno)


#############################
fig = plt.figure()
ax = fig.gca(projection='3d')

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(5, 15)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.savefig("apple_zmienne_r1_i_r2.jpg")
plt.show()
print("koniec")

#for i in range(3):
#    for j in range(1):
#        print(z[i,j])
