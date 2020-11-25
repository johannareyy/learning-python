"""decompor uma matriz em um produto de duas matrizes triangulares com zeros acima e abaixo da diagonal principal

 A * x * b       A = matriz de coeficientes a1,a2     x = vetor de variaveis x1,x2     b = vetor de termos independentes c1,c2

 transforma em L(U*x) = b            sendo L uma matriz triangular e U outra matriz triangular
       1) L*y = b  p descobrir o y=(U*x) 
       2) U*x = y  p descobrir x

       ex: [a00 a01]  =  [l00  0 ]  [1 u01]                                 [l 0 0]         [1 u u]
           [a10 a11]     [l10 l11]  [0  1 ]                             L = [l l 0]     U = [0 1 u]
                                                                            [l l l]         [0 0 1]
                      =  [l00     l00*u01   ]
                         [l10   l10*u01 +l11]

            ou seja como l00 = a00 e l10 = a10, todos os li0 valem ai0 (coluna zero do A = coluna 0 do L)
            dica: resolver primeiro termos onde i>=j (diagonalmente inferior)
            formula na aula 03.3

funcao decompoe = recebe a matriz A e retorna a matriz LU
funcao resolve = recebe LU e vetor b, faz substituiçao progressiva e regressiva e retorna o vetor x 
funcao faz tudo = chama as duas funcoes pra ficar mais elegante (se tiver so um sistema pra resolver)
"""

