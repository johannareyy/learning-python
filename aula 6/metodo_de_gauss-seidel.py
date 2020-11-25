"""quando n quiser uma grande precisão na solução, usa menos contas
# metodo de ponto fixo com varias variaveis

resolver o sistema linear Ax = b dado por
        E0  10*x0   -x1     2*x2         =  6
        E1  -x0     11*x1   -x2    3*x3  =  25
        E2  2*x0    -x1     10*x2  -x3   = -11
        E3          3*x1    -x2    8*x3  =  15

        isola o x0 na E0, x1 na E1, x2 na E2, x3 na E3
        k=numero do passo
        
        na E0:
        x0 do passo k, = 6 - (-x1 do passo k-1 + 2x2 do passo k-1)   nesse caso k-1 = 0 passo inicial
        dar um chute inicial bom para convergir
        se for diagonalmente dominante ela vai convergir, bom fazer desse jeito p ter certeza
"""