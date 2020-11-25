#Eliminacao Gaussiana(escalonamento)
#um dos poucos q n tem aproximacao (sem erro)

def equacao_linear(DIM, a, b): #receber matriz
    """
    Resolve o sistema linear por escalonamento
    Recebe: DIM=dimensão da matriz MxM, ou seja, mesmo numero de variaveis e equações   |1  2 -3  4 :  7 | a1=a1-(a1/a0)a0
            a=vetor de coeficientes                                                     |1  2  4  7 : -1 | j=i+1
            b=vetor de constantes                                                       |2  7  1  3 :  5 |
    Retorna: V=vetor resposta                                                           |8  3  2  1 :  2 |
    """
    i=DIM   #funcao length
    j=DIM+1
    V = 0 #coloquei isso pra n dar erro
    for i in a:
        for j in a:
            if a[i][i] == 0:
                continue #coloquei isso pra n dar erro
                #trocar linha
            if i > j:
                #escalonar
                a[i+1] -= a[i+1] - (a[i+1][0]/a[i][0])*a[i]

    #substituicao regressiva

    return V 