#achar raiz da função quadrática
# f(x) = x^2 - x - 1
# x^2 - x - 1 = 0  iguala a zero
# x = +- sqtr(x + 1) isola o x
# x = (x + 1)/x  outro modo de isolar o x
# g(x) = sqtr(x + 1) função auxiliar | só quero a raiz positiva
# da pra ter várias g(x), umas convergem mais rapido q outras, outras divergem.

import math

#g(x) = sqtr(x + 1)

p0 = 1  #chute inicial  
tol = 0.001 
erro = tol*10
val_antigo = 1 #chute inicial
val_novo = 2

while erro>tol:
    val_antigo = val_novo
    val_novo = math.sqrt(val_antigo + 1)
    erro = abs(val_novo - val_antigo)

print (val_novo, "  erro:", erro)

#g(x) = (x + 1)/x     ou     g(x) = 1 + 1/x

p0_2 = 1 #chute inicial entre intervalo [1,2]
tol_2 = 0.001
erro_2 = tol*10
val_antigo_2 = 1 #chute inicial
val_novo_2 = 2

while erro_2>tol_2:
    val_antigo_2 = val_novo_2
    val_novo_2 = 1 + 1/val_antigo_2
    erro_2 = abs(val_novo_2 - val_antigo_2)

print(val_novo_2, "  erro:", erro_2)