#Calcular ate atingir determinado erro
#Laco while
#Erro e tolerancia

i=1
tol=0.01 #1.0e-3 = 0.001 (isso vale pra todas as linguagens)
erro=10*tol #erro inicial maior q tol pra entrar no while

pi_anterior = 4.0
pi_atual = 4.0

numerador = -4
denominador = 3.0

while erro>tol:
    pi_atual = pi_anterior + numerador/float(denominador)
    erro = abs (pi_atual - pi_anterior) #modulo

    print(i,pi_atual, erro)

    numerador *= -1
    denominador += 2.0
    i += 1
    pi_anterior = pi_atual



print ("estou fora")