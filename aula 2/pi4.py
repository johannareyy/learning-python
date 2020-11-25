#grafico da convergencia
#adaptar pi1.py

import matplotlib.pyplot as plt

N=1000000


pi = 4.0
vetor_pi = [0]*N #0 em 1000000 casas
vetor_pi[0] = pi


numerador = -4
denominador = 3.0

for i in range(1,N):
    pi += numerador/denominador     #ou floar(denominador) se quiser evitar bugs

    numerador *= -1
    denominador += 2.0

    vetor_pi[i] = pi



plt.plot(vetor_pi)
plt.show