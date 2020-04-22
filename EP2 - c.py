# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def jacobi(A, b, nmax): #recebe a matriz de coeficientes e a matriz b do sistema Ax=b
    e = 0.001 #precisao
    n=len(A)
    m=len(b)
    D=np.zeros((n,n)) #matriz diagonal
    J=np.zeros((n,n)) #matriz J tal que x = Jx + c
    c=np.zeros(m) #matriz c tal que x = Jx + c
    for i in range(0,n):
        num = A[i][i]
        D[i][i] = num  #montando a matriz diagonal  
        for k in range(0,n):
            coef = -(A[i][k]/num) #montando a matriz J
            if k == i:
                coef=0 #os numeros na diagonal de J sao 0
            J[i][k] = coef 
        c[i]=(1/(D[i][i]))*b[i] #monta a matriz c
    #temos as matrizes J e C para que iteremos x = Jx + c    
    x = [0 for i in range(m)] #inicio a lista da solução
    a = [0 for i in range(m)] #lista auxiliar
    t=0
    dados = [] #lista de dados para anexar na tabela
    lista_dif = [0 for i in range(m)] #lista para calculo do erro
    while t<nmax:
        for i in range(m):
            a = x #atualizo a
            x = np.dot(J,x) + c #atualizo x com o método iterativo
            lista_dif[i]=(abs(a[i]-x[i])) #calculo o erro para cada variável
        dif = max(lista_dif) #escolho o maior numero para a condição de parada
        calc = [t, x[0], x[1], x[2], dif]
        dados += [calc]
        if dif < e: #condicao de parada
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
b=[14,5,0] #lista b
A=[[11,0,1], [0,5,-1], [1,-1,-1]] #matriz de coeficientes A
print(jacobi(A,b,20)) #aplicação do método com 20 iterações