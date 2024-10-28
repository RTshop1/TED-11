import random
VET = []
for i in range(10):
    numero = int(input(f"Digite o número {i + 1}: "))
    VET.append(numero)

repetidos = {}
for i in range(len(VET)):
    numero = VET[i]
    posicoes = [j for j in range(len(VET)) if VET[j] == numero]
    
    if len(posicoes) > 1 and numero not in repetidos:
        repetidos[numero] = posicoes

if repetidos:
    print("\nNúmeros repetidos e suas posições:")
    for numero, posicoes in repetidos.items():
        print(f"Número {numero} encontrado nas posições: {posicoes}")
else:
    print("\nNão há números repetidos no vetor.")

A = [[random.randint(1, 100) for _ in range(10)] for _ in range(10)]

print("\nMatriz A:")
for linha in A:
    print(linha)

soma_total = sum(sum(linha) for linha in A)
print(f"\nSoma de todos os valores da matriz A: {soma_total}")

B = [[valor * 3 for valor in linha] for linha in A]

print("\nMatriz B (A * 3):")
for linha in B:
    print(linha)