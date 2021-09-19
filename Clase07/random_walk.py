import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)    
    return pasos.cumsum()

N = 100000
camino_actual = randomwalk(N)
mas_alejado = camino_actual
menos_alejado = camino_actual
maximo = np.max(np.abs(camino_actual))
minimo = np.max(np.abs(camino_actual))

fig = plt.figure(1,figsize=(12,8),dpi=80)
plt.subplot(2,1,1)
plt.title(r'$12$ caminatas al azar')
plt.plot(camino_actual)

for i in range(11):
    camino_actual = randomwalk(N)
    plt.plot(camino_actual)
    maximo_actual = np.max(np.abs(camino_actual))
    if maximo_actual>maximo:
        mas_alejado = camino_actual
        maximo = maximo_actual
    elif np.max(np.abs(camino_actual))<minimo:
        menos_alejado = camino_actual
        minimo = maximo_actual
        
plt.ylim(-maximo-100,maximo+100)
plt.yticks(np.linspace(-(maximo//100)*100,(maximo//100)*100,3))

plt.xlabel('Tiempo')
plt.ylabel('Distancia al origen')
        
ax1 = plt.subplot(2,2,3)
plt.xticks([])
plt.title('La caminata que más se aleja')
plt.ylim(-maximo-100,maximo+100)
plt.plot(mas_alejado)

ax2 = plt.subplot(2,2,4)
plt.plot(menos_alejado)
plt.xticks([])
plt.yticks([])
plt.ylim(-maximo-100,maximo+100)
plt.title('La caminata que menos se aleja')

fig.tight_layout(pad=3.0)


plt.show()
