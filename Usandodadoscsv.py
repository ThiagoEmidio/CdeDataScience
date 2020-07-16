#crescimento população brasileira 1980-2016

import matplotlib.pyplot as plt

dados = open("populacao_brasileira.csv").readlines()

x=[]
y=[]

for i in range(len(dados)):
    if i != 0:
        linha=dados[i].split(";")
        x.append(int(linha[0]))
        y.append(int(linha[1]))

#print(x)
plt.bar(x,y)
plt.title("Crescimento populacional brasileiro")
plt.xlabel("Ano")
plt.ylabel("População em 100 mil hab.")
plt.show ()
