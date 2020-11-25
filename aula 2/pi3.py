#usar funcao
#reusabilidade

def calcula_pi(tol):
    """
    calcula o numero pi com a serie de Gregory-Leibnitz
    recebe: a tolerancia
    retorna: o pi e o erro
    """

    #inicializo com valor alto, pra entrar no laco
    erro=10000
    pi_anterior = 4.0
    pi_atual = 4.0

    numerador = -4
    denominador = 3.0

    while erro>tol:
        pi_atual = pi_anterior + numerador/float(denominador)
        erro = abs (pi_atual - pi_anterior) #modulo


        numerador *= -1
        denominador += 2.0
        pi_anterior = pi_atual
    
    return pi_atual, erro


pi,e = calcula_pi(1e-3)
print(pi,e)
#ou imprime direto
print(calcula_pi(1e-6))