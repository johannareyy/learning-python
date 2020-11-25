# -*- coding: utf-8 -*-
#utf-8 para executar acento


####### variáveis tem tipos definidas dinamicamente

x = 12
print(x)

x = "texto"     #ou 'texto', mas as vezes aspas simples dão erro em coisas específicas
print(x)






####### indentação (afastamento) e estruturas de controle (condicionais)
#sintaxe das condicionais

a = 19
b = 20

if a < b:
    print (a, "é menor que", b)
elif a == b:
    print (a, "é igual a", b)
else:
    print (a, "é maior que", b)

    while a < b:
        print(a, b)
        a = a * 2






####### listas (vetores)

c = [0, 1, 3, 5, 7]

print(c)    #imprime lista inteira
print(c[3])     #imprime posição 3
print(c[:3])    #imprime até posição 3
print(c[1:3])    #imprime da posição 1 até 3

c.append(10)    #adiciona elemento 10 na lista
print(c)

print("c tem", len(c), "elementos")     # https://docs.python.org/3/tutorial/datastructures.html






####### laço for

c = [0, 1, 3, 5, 7]

for x in c:
    print(x)

print("------------")
for i in range(5):
    print(i)






####### funções

def f1(x, y):
    print(x, y)

#f1(1, 2)
#f1("texto, 3")
#f1([1, 2, 3], "oi")

def f2(x, y):
    return x*y, x*x, y*y

a,b,c = f2(1, 2)
print(a, b, c)

def funcao_de_funcao( funcao, x, y):
    print( funcao(x, y))

funcao_de_funcao(f1, 0, 2)
funcao_de_funcao(f2, 0, 2)






####### biblioteca matemática

import math     # https:://docs.python.org/3/library/math.html

print(math.fabs(-2))

print(math.exp(3))
print(math.log(3))
print(math.log10(3))
print(math.pow(3, 4))
print(math.sqrt(3))
print(math.sin(0.5))

print(math.e)
print(math.pi)


