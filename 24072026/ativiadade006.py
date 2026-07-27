nota = float(input("Qual sua nota? "))
nota2 = float(input("Sua segunda nota? "))

media = (nota + nota2) / 2

if media >= 7:
    print("Aprovado")
elif media >= 5 and media <= 6.9:
    print("Recuperação")
elif media < 5:
    print("Reprovado") 