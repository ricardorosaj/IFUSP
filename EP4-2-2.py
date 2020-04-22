# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

def f(t,x,z): #sistema forcado
    return F*np.cos(t) + 0.5*x*(1-x**2) - 0.25*z

xgraf = [] #lista dos valores de x para plotar grafico
Fgraf = [] #lista dos valores de F para plotar grafico
for F in np.arange(0,0.28,0.0005):
    t = 0 #valor inicial para t0
    x = -1 #valor inicial para x(t0)
    z = 1 #valor inicial para z(t0)    
    h = 0.01*2*np.pi #tamanho do passo 
    for i in range(200000): #rotina sugerida
        k1x = h*z
        k1z = h*f(t,x,z)
        k2x = h*(z+k1z/2)
        k2z = h*(f(t+h/2,x+k1x/2,z+k1z/2))
        k3x = h*(z+k2z/2)
        k3z = h*(f(t+h/2,x+k2x/2,z+k2z/2))
        k4x = h*(z+k3z/2)
        k4z = h*(f(t+h,x+k3x,z+k3z))
        x = x + (k1x + 2*k2x + 2*k3x + k4x)/6
        z = z + (k1z + 2*k2z + 2*k3z + k4z)/6
        t = t + h
    h=0.001*2*np.pi  
    for i in range(0,100):
        for j in range(0,1000):
            k1x = h*z
            k1z = h*f(t,x,z)
            k2x = h*(z+k1z/2)
            k2z = h*(f(t+h/2,x+k1x/2,z+k1z/2))
            k3x = h*(z+k2z/2)
            k3z = h*(f(t+h/2,x+k2x/2,z+k2z/2))
            k4x = h*(z+k3z/2)
            k4z = h*(f(t+h,x+k3x,z+k3z))
            x = x + (k1x + 2*k2x + 2*k3x + k4x)/6
            z = z + (k1z + 2*k2z + 2*k3z + k4z)/6
            t = t + h
        xgraf.append(x) #adiciono os valores as respectivas listas
        Fgraf.append(F)  
#Montagem do grafico        
fig, ax = plt.subplots()
ax.scatter(Fgraf,xgraf,s=3)
ax.set(xlabel='F',ylabel="x", title='Diagrama de Bifurcação')  
plt.show                    