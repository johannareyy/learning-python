#Suponha que L = 3 m, r = 0.3 m e V = 0.25 m3. Use o Método da Bissecção para
#determinar a profundidade da água na gamela com precisão de 0.05 m. Use como
#precisão, no Método da Bissecção, a metade do intervalo no passo. (DICA: Como
#intervalo inicial de busca, considere o valor máximo e mínimo que h pode assumir).

import math

ValorMin = 1.69 #h = r = 0.3
ValorMax = -95.5 #h = 0
ValorMed = 

erro = 1000000
prec = 0.05 #tol

while erro>prec
    if (ValorMax + ValorMin)/2:
     