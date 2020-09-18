def bisseccao(F, A, B, TOL):
    """
    Encontra a raiz de F (em [A,B]) com um erro
    menor que TOL usando o algoritmo da Bissecção

    Recebe:
    F=Função para encontrar a raiz
    A,B=Intervalo de busca da raiz
    TOL=Valor máximo do erro(tolerância)

    Retorna:
    p=Raiz encontrada
    E=Erro
    """

    E = (B-A)/2.0
    p = (A+B/2.0)

    while E>TOL:
        if F(A)*F(p)<0: B = p
        else: A = p
        E = (B-A)/2.0
        p = (A+B)/2.0

    return p,E