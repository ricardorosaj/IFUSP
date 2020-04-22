# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

#item a
def f1(t,x,z): #funcao para potencial duplo
    return 0.5*x*(1-x**2)

h = 0.01 #tamanho do passo
t = 0 #valor inicial para t0
x = -1 #valor inicial para x(t0)
z = 0.5 #valor inicial para z(t0) (0.1,0.5,1.0)
n = 50000 #numero de pontos a se calcular
xgraf = []
zgraf = []
for i in range(n):
    k1x = h*z
    k1z = h*f1(t,x,z)
    k2x = h*(z+k1z/2)
    k2z = h*(f1(t+h/2,x+k1x/2,z+k1z/2))
    k3x = h*(z+k2z/2)
    k3z = h*(f1(t+h/2,x+k2x/2,z+k2z/2))
    k4x = h*(z+k3z/2)
    k4z = h*(f1(t+h,x+k3x,z+k3z))
    x = x + (k1x + 2*k2x + 2*k3x + k4x)/6
    z = z + (k1z + 2*k2z + 2*k3z + k4z)/6
    t = t + h
    xgraf.append(x)
    zgraf.append(z)
fig, ax = plt.subplots()
ax.plot(xgraf,zgraf)
ax.set(xlabel='x(t)',ylabel="x'(t)", title='Espaço de Fases')  
plt.show

#item b
def f2(t,x,z): #funcao com 2*gama = 0.25
    return 0.5*x*(1-x**2) - 0.25*z

h = 0.01 #tamanho do passo
t = 0 #valor inicial para t0
x = -1 #valor inicial para x(t0)
z = 1 #valor inicial para z(t0)
n = 5000 #numero de pontos a se calcular
xgraf = []
zgraf = []
for i in range(n):
    k1x = h*z
    k1z = h*f2(t,x,z)
    k2x = h*(z+k1z/2)
    k2z = h*(f2(t+h/2,x+k1x/2,z+k1z/2))
    k3x = h*(z+k2z/2)
    k3z = h*(f2(t+h/2,x+k2x/2,z+k2z/2))
    k4x = h*(z+k3z/2)
    k4z = h*(f2(t+h,x+k3x,z+k3z))
    x = x + (k1x + 2*k2x + 2*k3x + k4x)/6
    z = z + (k1z + 2*k2z + 2*k3z + k4z)/6
    t = t + h
    xgraf.append(x)
    zgraf.append(z)
fig, ax = plt.subplots()
ax.plot(xgraf,zgraf)
ax.set(xlabel='x(t)',ylabel="x'(t)", title='Espaço de Fases')  
plt.show

def f3(t,x,z): #funcao com 2*gama = 0.8
    return 0.5*x*(1-x**2) - 0.8*z

h = 0.01 #tamanho do passo
t = 0 #valor inicial para t0
x = -1 #valor inicial para x(t0)
z = 1 #valor inicial para z(t0)
n = 5000 #numero de pontos a se calcular
xgraf = []
zgraf = []
for i in range(n):
    k1x = h*z
    k1z = h*f3(t,x,z)
    k2x = h*(z+k1z/2)
    k2z = h*(f3(t+h/2,x+k1x/2,z+k1z/2))
    k3x = h*(z+k2z/2)
    k3z = h*(f3(t+h/2,x+k2x/2,z+k2z/2))
    k4x = h*(z+k3z/2)
    k4z = h*(f3(t+h,x+k3x,z+k3z))
    x = x + (k1x + 2*k2x + 2*k3x + k4x)/6
    z = z + (k1z + 2*k2z + 2*k3z + k4z)/6
    t = t + h
    xgraf.append(x)
    zgraf.append(z)
fig, ax = plt.subplots()
ax.plot(xgraf,zgraf)
ax.set(xlabel='x(t)',ylabel="x'(t)", title='Espaço de Fases')  
plt.show

#item c
F = 0.6 #coeficiente da forca
#transiente deve se esvanescer para t>>1/0.125
def f4(t,x,z): #sistema forcado
    return F*np.cos(t) + 0.5*x*(1-x**2) - 0.25*z

h = 0.01 #tamanho do passo
t = 0 #valor inicial para t0
x = -1 #valor inicial para x(t0)
z = 1 #valor inicial para z(t0)
n = 100000 #numero de pontos a se calcular
xgraf = []
zgraf = []
for a in range(200000): #retirar o transiente
    k1x = h*z
    k1z = h*f4(t,x,z)
    k2x = h*(z+k1z/2)
    k2z = h*(f4(t+h/2,x+k1x/2,z+k1z/2))
    k3x = h*(z+k2z/2)
    k3z = h*(f4(t+h/2,x+k2x/2,z+k2z/2))
    k4x = h*(z+k3z/2)
    k4z = h*(f4(t+h,x+k3x,z+k3z))
    x = x + (k1x + 2*k2x + 2*k3x + k4x)/6
    z = z + (k1z + 2*k2z + 2*k3z + k4z)/6
    t = t + h
for i in range(n): #rk4 para criar os espacos de fase
    k1x = h*z
    k1z = h*f4(t,x,z)
    k2x = h*(z+k1z/2)
    k2z = h*(f4(t+h/2,x+k1x/2,z+k1z/2))
    k3x = h*(z+k2z/2)
    k3z = h*(f4(t+h/2,x+k2x/2,z+k2z/2))
    k4x = h*(z+k3z/2)
    k4z = h*(f4(t+h,x+k3x,z+k3z))
    x = x + (k1x + 2*k2x + 2*k3x + k4x)/6
    z = z + (k1z + 2*k2z + 2*k3z + k4z)/6
    t = t + h
    xgraf.append(x)
    zgraf.append(z)
fig, ax = plt.subplots()
ax.plot(xgraf,zgraf)
ax.set(xlabel='x(t)',ylabel="x'(t)", title='Espaço de Fases')  
plt.show