import numpy as np
import matplotlib.pyplot as plt
#Constantes dadas no problema
k = 14.4 #eV angstrons
V0 = 667.0 #eV
r0 = 0.290 #angstrons
#Potencial
def V(x):
    return -(k/x) + V0*np.exp((-x)/r0)
#Força
def F(x):
    return -(k/(x**2)) + (V0/r0)*np.exp(-x/r0)
#Método que utiliza a diferença entre valores obtidos nas iterações como parâmetro de parada
def secante(a, b, tol):
    x0=a
    x1=b
    while np.abs(x1-x0) >= tol:
        x2 = x1 - F(x1)*((x1-x0)/(F(x1)-F(x0)))
        x0=x1
        x1=x2
        print(x2)
    return x2
#Aplicação do método com pontos x=2 e x=1 e com precisão 0.01
print(secante(2, 1, 0.01))

#Gráficos
x = np.arange(0.3, 7.0, 0.001)
y1 = V(x)
y2 = F(x)
#Gráfico do Potencial
fig, ax = plt.subplots()
ax.plot(x, y1)
plt.ylim(-8,6)
ax.set(xlabel='Distância (Å)', ylabel='Potencial (eV)', title='V(r) x r')
ax.grid()
plt.show()
#Gráfico da Força
fig, ax = plt.subplots()
ax.plot(x, y2)
plt.ylim(-8,6)
ax.set(xlabel='Distância (Å)', ylabel='Força (eV/Å)', title='F(r) x r')
ax.grid()
plt.show()
