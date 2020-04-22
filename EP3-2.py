# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

l = 1   #defino valores para l e g
g = 10
k_1 = np.sqrt(l/g) #raiz de l/g
dados = [] #lista dos dados para montar tabela

T_gal = 2*np.pi*k_1 #periodo do pendulo de Galileu

def trapezio(a,b,N=1000): #metodo dos trapezios
    h = (b-a)/N #tamanho do intervalo para pontos equidistantes
    soma = 0 
    for i in range(0,N):
        x = a + i*h  #calculo o valor de cada x para os extremos dos intervalos
        soma += 2*f(x) #para pontos equidistantes, I = h/2*[f1+2f2+...+2fn+fn+1]
    soma += f(a) + f(b)    
    return soma*h/2

def f(x): #função para periodo do pêndulo dada
    return 4*k_1*(1/(np.sqrt(1-(k**2)*(np.sin(x))**2)))

for i in np.arange(0.15,np.pi,0.15): #para 20 valores de θ_0, calculo T
    theta_0 = i #novo valor de θ
    k = np.sqrt((1-np.cos(theta_0))/2) #novo valor para a constante k, dependente de θ_0
    T = trapezio(0,np.pi/2) #novo valor para T
    dados.append([theta_0,T]) #adiciono na lista de dados os valores de θ_0 e T

#Montagem da tabela
col = ('θ_0','T') 
table = plt.table(cellText=dados,colLabels=col,loc='top')
plt.axis('off')
table.scale(2.0,1.5)
table.auto_set_font_size(False)
table.set_fontsize(11)
plt.show    
    
#Montagem do gráfico
theta_0 = np.arange(0, np.pi, 0.001)
k = np.sqrt((1-np.cos(theta_0))/2)
T = trapezio(0,np.pi/2)
y = T/T_gal
fig, ax = plt.subplots()
ax.plot(theta_0, y)
plt.ylim(0,6)
ax.set(xlabel='θ_0', ylabel='T/T_gal', title='Razão entre os períodos')
ax.grid()
plt.show()