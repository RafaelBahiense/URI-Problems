n = int(input())
regioes = int(((n*(n-1))/2)+((n*(n-1)*(n-2)*(n-3))/24)+1)
print(regioes)
# A fórmula acima é a fórmula de Euler para poliedros convexos (V-E+F=2) e adaptada 
# ao escopo do problema com aplicação da combinação de n tomado de 2 a 2 (V) 
# e combinação n tomado 4 a 4 (E)
# https://www.youtube.com/watch?v=K8P8uFahAgc
