import numpy as np
#Função dada
def f(x):
    return x**3-np.cos(x**2)
#Derivada da função dada
def derivada(x):
    return 3*x**2 + 2*x*np.sin(x**2)
#Método utilizando um ntot de iterações e uma estimativa inicial
def newton(estimativa,ntot):
    xn=estimativa
    n=1
    while n<ntot:
        xn1=xn-f(xn)/derivada(xn)
        xn=xn1
        n+=1
        print(xn1)
    return xn1
#Aplicação do método com chute inical x=0.2 e 10 iterações
print(newton(0.2,10))