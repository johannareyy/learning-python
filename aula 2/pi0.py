#Calcula pi para N termos da série
#Variáveis
#Estrutura 
#pi = 4 (1/1 - 1/3 + 1/5 - 1/7 + 1/9 -...)
#pi = somatoria de (-1)^i/2i + 1

N = 1000000
pi = 4.0

for i in range(1,N):
    pi = pi + 4*(-1)**(i)/float(2*i+1)        #como em py a tipagem e dinamica, convem transformar em float pro resultado ser em float

    print(i,pi)
