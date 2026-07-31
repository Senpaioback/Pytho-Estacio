soma = 0

# O laço vai rodar exatamente 6 vezes
for numero in range(0, 10):
    
    # Verifica se o número é par
    if numero % 2 == 0:
        soma += numero  # Soma o número atual ao total da soma

print(f"A soma apenas dos números pares digitados é: {soma}")
