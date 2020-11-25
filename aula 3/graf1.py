#site
#grafico simples e conceitos fundamentais
#listas em python

import matplotlib.pyplot as plt
#import = include em C
#pyplot sub biblioteca do matplotlib
#as plt pra chamar por um apelido, pode dar o nome quiser

plt.plot([1.1, 1.2, 5.6, 8], [1, 2, 3, 4], "ro-") #se n der o x ele usa o indice da lista # r=read, o=plotar pontos como bolinhas, -=conectar os pontos por linhas
plt.ylabel('alguns números') #descricao do y

plt.show()
plt.savefig("gráfico.png")