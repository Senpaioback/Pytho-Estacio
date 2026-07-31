# Passo 1: Receber as entradas do usuário
primeiro = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

# Passo 2: Calcular o décimo termo para definir o limite do loop
# Fórmula do enésimo termo: an = a1 + (n - 1) * r
decimo = primeiro + (10 - 1) * razao

# Passo 3: Loop que anda de "razao" em "razao" até o décimo termo
print("Os 10 primeiros termos são:")
for termo in range(primeiro, decimo + razao, razao):
    print(termo, end=" → ")
print("FIM")
