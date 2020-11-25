#uma das tecnicas p fazer ajustes de função (melhor funcao q descreve o grafico dos dados)
#analizar/descrever dados experimentais
#menor erro ao quadrado pq grafico do modulo n é suave
import math

#com linha, fazer um com grau maior do polinomio

def minimosQuadrados(x, y):

    somax = 0
    somay = 0
    xvezesy = 0
    somaxquadrado = 0
    m = 1 #descobrir q q é isso

    for i in x:
        somaxquadrado += math.pow(i,2)
        somax += i
    for i in y:
        somay += i
    xvezesy = x*y #fazer de um modo q fique somadexvezesy

    a0 = (somaxquadrado*somay-xvezesy*somax)/(m*somaxquadrado-math.pow(somax,2))
    a1 = (m*xvezesy-somax*somay)/(m*somaxquadrado-math.pow(somax,2))

    return a0, a1


tabelax = [1,2,3,4]
tabelay = [1,2,3,4]

plotargrafico = minimosQuadrados(tabelax,tabelay)
