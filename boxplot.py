import matplotlib.pyplot as plt
import random

#vetor = [1,2,3,4,6,12,512,12,2]
vetor = []

for i in range(100):
    numero_aleatorio = random.randint(0,50)
    vetor.append(numero_aleatorio)

plt.boxplot(vetor)
plt.show()