'''
Método de Neville: polinomio de lagrange adaptado pra ser aplicado numericamente 
interpolação
a funcao vai passar em cima de todos os dados
se tenho n pontos, posso um polinomio de grau = n-1 
    ex=para 2 pontos, so posso passar UM polinomio de primeiro grau (reta)
    Lo = x-x1/xo-x1
    L1 = x-x0/x1-xo

    P(x)=yo*Lo + y1*L1

Em polinomios de grau maior funciona do mesmo jeito
    ex=grau 5, no ponto -> pula o 3
    Lo = (x-xo)/(x3-xo) * (x-x1)/(x3-x1) * (x-x2)/(x3-x2) * (x-x4)/(x3-x4) * (x-x5)/(x3-x5)
    dae repete isso pra todos os L1,L2
    coloca na equacao yo*Lo + y1*L1 + ...
    '''