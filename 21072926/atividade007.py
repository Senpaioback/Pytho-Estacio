nome = input("Nome: ")
ano = int(input("Ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(nome, "o ano é bissexto!")
else:
    print(nome, "o ano NÃO é bissexto.")