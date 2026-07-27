print("====Pedra, Pepel, Tesoura==== \n1 - Tesoura \n2 - Papel \n3 - Pedra")
opcao = (input("Escolha uma opção: "))

tesoura = 1
papel = 2
pedra = 3

if opcao == "1" and 1 < 2:
    print("Tesoura ganha de Papel")
elif opcao == "2" and 2 < 3:
    print("Papel ganha de Pedra")
elif opcao == "3" and 3 > 1:
    print("Pedra ganha de Tesoura")