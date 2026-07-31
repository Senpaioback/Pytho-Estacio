# Lendo os dados de entrada
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))

termo = primeiro
cont = 1

# Laço para mostrar os 10 primeiros termos
while cont <= 10:
    print(f"{termo}", end=" -> ")
    termo += razao
    cont += 1

print("FIM")