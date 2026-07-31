# Inicializando as variáveis
num = 0
cont = 0
soma = 0

# Leitura do primeiro número fora do laço
num = int(input("Digite um número [999 para parar]: "))

# Enquanto o número digitado NÃO for a flag (999)
while num != 999:
    soma += num
    cont += 1
    # Leitura do próximo número no final do laço
    num = int(input("Digite um número [999 para parar]: "))

print(f"Você digitou {cont} números e a soma entre eles foi {soma}.")