num = int(input("Digite um numero: "))
num2 = int(input("Digite o segundo numero: "))

if num > num2:
    print(f"Esse numero é maior {num}")
elif num2 > num:
    print(f"Esse numero é maior {num2}")
else:
    print("Ambos são iguais")