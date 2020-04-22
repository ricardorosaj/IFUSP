# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

#Item A
dados_simples=[] #tabela de dados para precisao simples
dados_duplos=[] # tabela de dados para precisao dupla
I = 5 #valor analitico da integral
y1 = [] #lista de valores de erro para precisao simples para o item D
y2 = [] #lista de valores de erro para precisao dupla para o item D

def f_1(x): #funcao utilizada na integracao
    return np.float32(6-6*(x**5))

def simpson_simples(a,b,p): #metodo de simpson
    N = 2**p #numero de intervalos
    h = np.float32((b-a)/N) #tamanho de cada intervalo
    soma = np.float32(0.0) #defino a soma
    for i in range(1,N):
        x = np.float32(a + i*h) #calculo o valor de cada x para os extremos dos intervalos
        if i%2 == 0: #se x_i tem indice par
            soma += 2*f_1(x)
        else: #se x_i tem indice impar
            soma += 4*f_1(x)
    soma += f_1(a) + f_1(b) #no final, temos f(a)+4f(x_1)+2f(x_2)+ ...+f(b)
    soma = h/3*soma #multiplico pelo fator h/3 do método de simpson
    return soma #retorno o valor da integral em precisao simples

#Item B
for i in range(1,26): #percorre p de 1 a 25 para plot da tabela
    p = i
    N = 2**p
    Inum_1 = simpson_simples(0,1,i)
    erro_1 = abs(Inum_1 - I)
    dados_simples.append([p,N,Inum_1,erro_1]) #acrescento os dados na lista de dados
    y1.append(erro_1)
    
#Montagem da tabela    
col = ('p','N', 'I_num', 'erro') 
table_1 = plt.table(cellText=dados_simples,colLabels=col,loc='top')
plt.axis('off')
table_1.scale(2.0,1.5)
table_1.auto_set_font_size(False)
table_1.set_fontsize(11)
plt.show()

#Item C
def f_2(x):
    return 6-6*(x**5)

def simpson_duplo(a,b,p): #metodo de simpson
    N = 2**p #numero de intervalos
    h = (b-a)/N #tamanho de cada intervalo
    soma = 0 #defino a soma 
    for i in range(1,N):
        x = a + i*h #calculo o valor de cada x para os extremos dos intervalos
        if i%2 == 0: #se x_i tem indice par
            soma += 2*f_2(x)
        else: #se x_i tem indice impar
            soma += 4*f_2(x)
    soma += f_2(a) + f_2(b) #no final, temos f(a)+4f(x_1)+2f(x_2)+ ...+f(b)
    soma = h/3*soma
    return soma #retorno o valor da integral em precisao dupla

for i in range(1,26): #percorre p de 1 a 25 para plot da tabela
    p = i
    N = 2**p
    Inum_2 = simpson_duplo(0,1,i)
    erro_2 = abs(Inum_2 - I)
    dados_duplos.append([p,N,Inum_2,erro_2]) #acrescento os dados na lista de dados
    y2.append(erro_2)
    
#Montagem da tabela    
col_1 = ('p','N', 'I_num', 'erro') 
table_2 = plt.table(cellText=dados_duplos,colLabels=col_1,loc='top')
plt.axis('off')
table_2.scale(2.0,1.5)
table_2.auto_set_font_size(False)
table_2.set_fontsize(11)
plt.show()

#Item D
fig, ax = plt.subplots()
x = np.arange(1,26,1)
ax.plot(x,y1,color='red',label='Simples')
ax.plot(x,y2,color='blue',label='Dupla')
ax.set(xlabel='p', ylabel='Erro', title='Erro(p) para precisão simples e dupla')
ax.set_yscale('log')
ax.legend(['Simples', 'Dupla'], loc=0)
ax.grid()
plt.show()