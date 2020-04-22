# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

#Item A
def f(x): #defino a funcao primeiro quadrante do circulo unitario
    return np.sqrt(1-x**2) 

def monte_carlo(seed_x, seed_y):
    cont_dentro = 0 #contador para pontos dentro do circulo
    cont_total = 0 #contador para o total de pontos
    a=16807
    m=2147483647
    for i in range(0,100):
        seed_x = (a*seed_x)%m #aplico LCG para x
        rand_x = seed_x/m
        seed_y = (a*seed_y)%m #aplico LCG para y
        rand_y = seed_y/m
        if rand_y <= f(rand_x): #se o ponto gerado esta dentro do circulo:
            cont_dentro+=1 #somo o numero de pontos dentro e o total
            cont_total+=1
        else: #se não:
            cont_total+=1
    return 4*(cont_dentro/cont_total) #retorna 4x a razao entre os pontos dentro e o total

#Item B
seed_x = 10300636 #seed para os valores de x
seed_y = 10030065 #seed para os valores de y
print(monte_carlo(seed_x, seed_y))

#Item C
dados = [] #lista de dados para criar tabela
n = 2 #iteracao para imprimir tabela
I_m = 0 #valor medio da integral
soma_I = 0 #variavel para somar valores de I_m
dif_I = 0 #diferenca entre I_m e I
soma_dif = 0 #variavel para somar valores de dif_I
while n<=131072:
   seed_x += 1 #modifico a seed para x
   seed_y += 1 #modifico a seed para y
   I = monte_carlo(seed_x, seed_y) #calculo a integral pelo metodo de monte carlo
   soma_I += I #calculo a soma para os valores de I
   I_m = soma_I/n #e a media
   dif_I = (I_m - I)**2 #calculo a diferenca para calcular sigma
   soma_dif += dif_I #calculo a soma para os valores de dif_I
   σ = np.sqrt(soma_dif/(n-1)) #calculo σ
   σ_m = σ/np.sqrt(n) #calculo σ_m
   if (n & (n-1) == 0) and n != 0: #se a iteracao eh uma potencia de 2
       dados.append([n, I_m, σ, σ_m]) #adiciono os valores calculados na lista de dados
   n += 1
   
#Motando a tabela   
col = ('N_tent','I_m','σ','σ_m') 
table = plt.table(cellText=dados,colLabels=col,loc='top')
plt.axis('off')
table.scale(2.0,1.5)
table.auto_set_font_size(False)
table.set_fontsize(11)
plt.show    