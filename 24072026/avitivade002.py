num = int(input("Digite um numero: "))
print("\nO que deseja conveter \n1 - Binirio \n2 - Octal\n 3 - Hexadecimal")
opcao = (input("Escolha uma opção: "))

if opcao == "1":
    binario = f"{num:b}"
    print(binario)
elif opcao == "2":
    octal = f"{num:o}"
    print(octal)
elif opcao == "3":
    hex = hex(num)
    print(hex)
else:
    print("Opção invalida")
