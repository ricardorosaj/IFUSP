# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def gauss_seidel(A, b, nmax):
    n = len(b)
    e=0.001
    L = np.tril(A) #matriz triangular inferior
    U = A - L #matriz 'triangular superior'
    x = [0 for i in range(n)] #chute inicial
    lista_dif = [0 for i in range(n)] #lista para calculo do erro
    dados= [] #lista de dados pra anexar na tabela
    t=0
    a = x #variável auxiliar
    while t<nmax:
        a=x #atualizo a
        x = np.dot(np.linalg.inv(L), b - np.dot(U, x)) #x=L^(-1)*(b-(U*x)) (metodo iterativo)
        for i in range(n):
            lista_dif[i] = (abs(a[i]-x[i])) #calculo o erro de cada variável
        dif = max(lista_dif) #na condição de parada pego o maior erro possível
        calc = [t, x[0], x[1], x[2], dif]
        dados += [calc]
        if dif<e: #condicao de parada
            col = ('k','I1','I2','I3','Erro') #montagem da tabela
            table = plt.table(cellText=dados,colLabels=col,loc='top')
            plt.axis('off')
            table.scale(2.0,1.5)
            table.auto_set_font_size(False)
            table.set_fontsize(11)
            plt.show   
            break
        t+=1
    return x    
b=[14,5,0] #vetor b do sistema
A=[[11,0,1], [0,5,-1], [1,-1,-1]] #matriz de coeficientes
print(gauss_seidel(A,b,10)) #aplico o método com um total de 10 iterações