# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def f(t,x,z): #sistema forcado
    return 0.28*np.cos(t) + 0.5*x*(1-x**2) - 0.25*z

t = 0 #valor inicial para t0
x = -1 #valor inicial para x(t0)
z = 1 #valor inicial para z(t0)    
h = 0.001*2*np.pi #tamanho do passo
xgraf=[]
zgraf=[] 
for i in range(200000):
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
for i in range(0,20000):
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
    xgraf.append(x)
    zgraf.append(z)  
fig, ax = plt.subplots()
ax.scatter(xgraf,zgraf,s=3)
ax.set(xlabel='x(t)',ylabel="x'(t)", title='')  
plt.show

