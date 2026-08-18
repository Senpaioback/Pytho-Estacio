lista = []

maior = None
menor = None

for cont in range(0, 5):
    # 1. Lemos o valor e guardamos na variável 'numero'
    numero = int(input("Digite um valor: "))
    lista.append(numero)

    # 2. Fazemos o teste AGORA, ainda dentro do for (repare no alinhamento/indentação)
    if maior is None:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

print(f"Maior: {maior}")
print(f"Menor: {menor}")
