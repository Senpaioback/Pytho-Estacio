# Passo 1: Ler o número inteiro
num = int(input("Digite um número inteiro: "))
tot = 0  # Contador de divisores

# Passo 2: Contar quantos divisores o número possui
for c in range(1, num + 1):
    if num % c == 0:
        tot += 1

# Passo 3: Verificar se é primo com base no total de divisores
if tot == 2:
    print(f"O número {num} é PRIMO!")
else:
    print(f"O número {num} NÃO É PRIMO! (Foi dividido {tot} vezes)")
