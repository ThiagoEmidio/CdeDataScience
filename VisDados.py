#visualização dos dados em python

import matplotlib.pyplot as plt

x=[1,2, 3,4,5,6]
y=[2,3,7,0,1,1]
titulo ="Gravido de barras"
eixoxis="Eixo x"
eixoipsolon="Eixo Y"

#Legendas
plt.title(titulo)
plt.xlabel(eixoxis)
plt.ylabel(eixoipsolon)

#plt.plot(x,y), é o pra grafico de linha
#plt.bar(x,y), é o pra grafico de barras
plt.bar(x,y)

plt.show()
