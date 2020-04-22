# -*- coding: utf-8 -*-
def gauss(A):
    n = len(A)
    for i in range(0, n):
        # Procuro pelo maior numero na linha i
        maior = abs(A[i][i])
        l_maior = i
        for k in range(i+1, n):
            # Caso tenha algum numero maior em uma linha k, substituo
            if abs(A[k][i]) > maior:
                maior = abs(A[k][i])
                l_maior = k
        # Coluna por coluna, troco a linha que tenho o máximo pela linha atual
        for k in range(i, n+1):
            a = A[l_maior][k]
            A[l_maior][k] = A[i][k]
            A[i][k] = a
        # Atualizo os termos de cada coluna e linha, zerando os números na
        # mesma coluna do maior número
        for k in range(i+1, n):
            c = -A[k][i]/A[i][i]
            for j in range(i, n+1):
                A[k][j] += c * A[i][j]   
    # De trás para frente, resolvo o sistema linear da matriz A na forma triangular superior
    x = [0 for i in range(n)]
    for i in range(n-1, -1, -1):
        x[i] = A[i][n]/A[i][i]
        for k in range(i-1, -1, -1):
            A[k][n] -= A[k][i] * x[i]
    return x
#Resolvendo o problema do EP com a matriz dada
a=[[0,5,-1,5], [11,0,1,14], [1,-1,-1,0]]
print(gauss(a))    