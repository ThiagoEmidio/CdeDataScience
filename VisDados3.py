#visualização dos dados em python

import matplotlib.pyplot as plt

x1=[1,3,5,7,9]
y1=[2,3,7,0,1]
x2=[2,4,6,8,10]
y2=[5,1,4,3,10]

titulo ="Scatterplot:Graficos de disperção/pontos"
eixoxis="Eixo x"
eixoipsolon="Eixo Y"

#Legendas
plt.title(titulo)
plt.xlabel(eixoxis)
plt.ylabel(eixoipsolon)


#plt.plot(x,y), é o pra grafico de linha
#plt.bar(x,y), é o pra grafico de barras
#plt.scatter(x,y), é o pra grafico de barras
plt.scatter(x1,y1, label="meuspontos", color="red")
plt.plot(x1,y1)

#plt.legend() dá as labels nos graficos
plt.legend()
plt.show()
