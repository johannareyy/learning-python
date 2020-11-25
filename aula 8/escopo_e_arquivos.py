#Com objetos mutaveis (quando muda o valor ele cria outro lugar e aponta pra ele)
x = 42
x = x + 1
y = x
x = 10
print(x is y)
#False



#Com objetos mutaveis (muda o valor do proprio lugar)
x = [1, 2, 3]

x = [1, 2, 3]
y = x
print(y is x)
#True



#Copiando conteudo
x = [1, 2, 3]
y = x[:]  #copia todo mundo do x, funciona so pra lista
print (y is x)  #como copia apenas o conteudo e n aponta pro mesmo lugar
#False

#tem funcao pra isso
import copy
x = [1, 2, 3]
y = copy.copy(x)   #tem um comando copy q copia qualquer coisa, n so listas
print(y is x)
#False

x = [[1,2], [3,4]]
y = copy.copy(x)
print (y is x)  #n copia a matriz, so os vetores
#False 
print (y[0] is x[0])
#True

x= [[1, 2], [3, 4]]
y = copy.deepcopy(x)
print(y[0] is x[0]) #copia o objeto lista dentro do objeto lista
#False


#Como ler arquivos de dados

import numpy as np

nome = "dados.txt"

M = np.loadtxt(nome, dtype='float', comments='#') #le arquivos de texto, ignora comentarios e linhas vazias
print(M)

#pegar coluna 0 e coluna 2 em vetores ("desempacotar")
x,z = np.loadtxt(nome,dtype='float', comments='#', usecols=(0, 2), unpack=True)
print(x)
print(z)
# http://docs.scipy.org/doc/numpy/reference/generated/numpy.loadtxt.html
# nesse link tem mais parametros q pode usar, tipo se os dados tao separados por '   ' ou ; ou |


