i = 0

while i  != 6:
        genero = input("digite seu genero (F/M)").lower()
        if genero == "f":
            print("Seu genero é feminino")
            break
        elif genero == "m":
            print("Seu genero é masculino")
            break
        else:
            print("Não corresponde")
