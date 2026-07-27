ano_nascimento = int(input("Ano de Nascimento: "))

ano_atual = 2026
idade = ano_atual - ano_nascimento
print(idade)

if idade <= 9:
    print("Mirim")
elif idade <= 14:
    print("Infantil")
elif idade <= 19:
    print("Junior")
elif idade <= 20:
    print("Senior")
else:
    print("Mestre")
