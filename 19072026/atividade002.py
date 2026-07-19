numero = str(input("Digite um número: "))

# Adicionamos "0000" na frente e pegamos apenas os últimos 4 caracteres
numero_formatado = ('0000' + numero)[-4:]

print(f"unidade: {numero_formatado[3]}")
print(f"dezena: {numero_formatado[2]}")
print(f"centena: {numero_formatado[1]}")
print(f"milhar: {numero_formatado[0]}")