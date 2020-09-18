import matplotlib.pylab as plt
import numpy as np

def P2(x,a):
    """
    Calcula um polinômio de ordem 2
    P2(x) = a0 + a1*x + a2*x**2

    Recebe:
    x=Escalar ou vetor onde calcular P2
    a=Vetor com coeficientes

    Retorna:
    Polinômio calculado em x
    """
    return(a[0] + a[1]*x + a[2]*x*x)

x = np.linspace(-1, 1, 100)     #(inicio_do_intervalo, final_do_intervalo, quantos_pontos_quero_no_intervalo)
#print(x)
#print(len(x))

#print(P2(x, [0, 0, 1]))        #pra cada x calcula um y

plt.plot(x, P2(x, [0, 0, 1]), "b.", label="$P_2(x) = x²$")      #"$$" = formatacao latec, pode usar um texto normal se quiser 
plt.plot(x, P2(x, [2, -1, 3]), "r-", label="$P_2(x) = 2 - x + 3x²$")

plt.grid()  #pra ter o gridzinho (quadriculado)
plt.margins(0.1)    #pra dar um espaço antes de comecar o gráfico
plt.legend()    #pra colocar o label
plt.show()  #pra mostrar na tela