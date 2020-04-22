import numpy as np
import matplotlib.pyplot as plt
#Definir a função dada no problema
def f(x):
    return x**3-np.cos(x**2)
#Método de Bissecção
def bissec(a,b,epsilon):
    xa = a
    xb = b
    while np.abs(xa-xb)>=epsilon: #tamanho do intervalo >= precisão
        c=(xa+xb)/2
        if f(a)*f(c)<0:
            xb=c
            print(xb)
        else:
            xa=c
            print(xa)
    return c        
#Aplicação do método com intervalo [-1,1] e precisão 0.001
print(bissec(-1,1,0.001))       
#Código para plotar o gráfico da função dada
x = np.arange(-5, 5, 0.01)
fig, ax = plt.subplots()
ax.plot(x, f(x))
plt.ylim(-8,8)
ax.set(xlabel='X', ylabel='f(x)', title='x^3 - cos(x^2)')
ax.grid()
plt.show()