#boas praticas de programacao, melhorar eficiencia do calculo, nomes com sentido
#pin = pin-1 + 4(-1)^n/2n+1


N=100
pi = 4.0

numerador = -4
denominador = 3.0

for i in range(1,N):
    pi += numerador/denominador     #ou floar(denominador) se quiser evitar bugs

    numerador *= -1
    denominador += 2.0


print(i,pi)