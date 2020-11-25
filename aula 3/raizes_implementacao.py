import raizes

def funcao(x):
    return x*x - 5.0

def funcao2(x):
    return x*x - 2.0

p,E = raizes.bisseccao(funcao, 0.0, 3.0, 1e-10)
print("Solução: p ≃ ", p, " +- ", E)

p,E = raizes.bisseccao(funcao2, 0.0, 2.0, 1e-6)
print("Solução: p ≃ ", p, " +- ", E)