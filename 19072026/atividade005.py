frase = input("Digite uma frase: ").strip().upper()

print(f"A quantidade de 'A': {frase.count('A')}")
# + 1 aqui para a posição fazer sentido para quem lê:
print(f"A primeira vez que aparece na posição: {frase.find('A') + 1}")
print(f"A ultima aparição do A é na posição: {frase.rfind('A') + 1}")

