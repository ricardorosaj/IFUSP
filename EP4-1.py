# -*- coding: utf-8 -*-

def f1(t,y,z): #defino a funcao z'
    return z - y + t**3 - 3*t**2 + 6*t

def f2(z): #defino a funcao x'
    return z

#Metodo de Euler

h = 0.01 #tamanho do passo
t = 0 #valor inicial para t0
y = 0 #valor inicial para y(t0)
z = 0 #valor inicial para z(t0)
n = 601 #numero de pontos a se calcular

for i in range(n):
    z = z + h*f1(t,y,z) #atualizo o valor de z
    y = y + h*f2(z) #atualizo o valor de y
    t = t + h #atualizo o valor de t
    if i==600: #imprimo o resultado para t=6
        print(z,y) #printo y'(6) e y(6)
        print('erro',abs(3*6**2-z),abs(6**3-y))

#Runge-Kutta de 4ª ordem
h = 0.01 #tamanho do passo
t = 0 #valor inicial para t0
y = 0 #valor inicial para y(t0)
z = 0 #valor inicial para z(t0)
n = 601 #numero de pontos a se calcular
for i in range(n): #aplico a subrotina designada no ep
    k1y = h*z
    k1z = h*f1(t,y,z)
    k2y = h*(z+k1z/2)
    k2z = h*(f1(t+h/2,y+k1y/2,z+k1z/2))
    k3y = h*(z+k2z/2)
    k3z = h*(f1(t+h/2,y+k2y/2,z+k2z/2))
    k4y = h*(z+k3z/2)
    k4z = h*(f1(t+h,y+k3y,z+k3z))
    y = y + (k1y + 2*k2y + 2*k3y + k4y)/6
    z = z + (k1z + 2*k2z + 2*k3z + k4z)/6
    t = t + h
print(z,y)    #printo y'(6) e y(6)

print('erro',abs(3*6**2-z),abs(6**3-y))