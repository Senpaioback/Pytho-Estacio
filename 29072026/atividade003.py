opcao = ""

# O loop roda ENQUANTO a opção for DIFERENTE de "5"
while opcao != "5":
    print("\n===== MENU =====")
    print("1 - Soma")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Sair")
    
    opcao = input("Escolha uma opção: ")

    # Se a pessoa escolher sair, não precisamos pedir os números
    if opcao == "5":
        print("Saindo do programa...")
    elif opcao in ["1", "2", "3", "4"]:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if opcao == "1":
            print(f"Resultado: {num1 + num2}")
        elif opcao == "2":
            print(f"Resultado: {num1 - num2}")
        elif opcao == "3":
            print(f"Resultado: {num1 * num2}")
        elif opcao == "4":
            if num2 != 0:
                print(f"Resultado: {num1 / num2}")
            else:
                print("Erro: Não é possível dividir por zero!")
    else:
        print("Opção inválida! Tente novamente.")