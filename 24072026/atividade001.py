valor_casa = float(input("Qual valor da casa? "))
salario_comprador = float(input("Qual seu salario? "))
anos_pagamento = int(input("Quantos anos vai pagar? "))
porcentagem = 30

calculo1 = (porcentagem / 100) * salario_comprador
calculo2 = valor_casa / (anos_pagamento * 12)

print(calculo1, calculo2)

if calculo2 <= calculo1:
    print("Voce consegue comprar essa casa")
else:
    print("Voce não consegue comprar essa casa")