lista = []

while True:
    lista.append(int(input("Digite um valor: ")))
    escolha = input("Deseja continuar (S/N): ").strip().upper()

    if escolha == "N":
        break


    