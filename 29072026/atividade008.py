resp = "S"
soma = quant = media = maior = menor = 0

while resp in "Ss":
    num = int(input("Digite um número: "))
    soma += num
    quant += 1

    # Na primeira repetição, o próprio número é o maior e o menor
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]

media = soma / quant

print(f"Você digitou {quant} números e a média foi {media:.2f}")
print(f"O maior valor foi {maior} e o menor foi {menor}")