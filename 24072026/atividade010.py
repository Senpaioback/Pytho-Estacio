print("O laptop custa R$ 2.500 \n=====Forma de Pagamento===== \n1 - A vista \n2 - A vista no Cartão \n3 - 2x no cartão \n4 - 3x no cartão ou mais")

laptop = 2500.00

opcao = input("Escolha uma forma de pagamento: ")

if opcao == "1":
    desconto = 10
    preco_final = laptop * (1 - desconto / 100)
    print(f"O preço final do laptop ficou R$ {preco_final:.2f}")

elif opcao == "2":
    desconto = 5
    preco_final = laptop * (1 - desconto / 100)
    print(f"O preço final do laptop ficou R$ {preco_final:.2f}")

elif opcao == "3":
    parcela = laptop / 2
    print(f"Preço normal de R$ {laptop:.2f} em 2x de R$ {parcela:.2f}")

elif opcao == "4":
    juros = 20
    preco_final = laptop * (1 + juros / 100)
    print(f"Preço final com juros: R$ {preco_final:.2f}")

else:
    print("Opção inválida!")