maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input(f"Peso da {p}ª pessoa: "))

    # Na primeira repetição, o primeiro peso é tanto o maior quanto o menor
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f"\nO maior peso lido foi de {maior}kg")
print(f"O menor peso lido foi de {menor}kg")