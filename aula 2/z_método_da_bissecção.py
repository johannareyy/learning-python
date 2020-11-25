#considere o seguinte produtório
#Z=pi i de 1 a n z1
#onde z1=(-1)**2i+1/sqtr(i)
import math

Z = 1
n = 10

numerador = -1.0
denominador = 1.0

for i in range(1,n):
    Z *= numerador/float(math.sqrt(denominador))

    denominador += 1.0 

print(Z)