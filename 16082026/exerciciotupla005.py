valores = []

while True:
    resposta = input("Digite um número (ou 'sair' para terminar): ")
    
    # Verifica se o usuário quer encerrar o programa
    if resposta.lower() == 'sair':
        break
        
    numero = int(resposta)
    
    # Só adiciona se o número ainda não estiver na lista
    if numero not in valores:
        valores.append(numero)
    else:
        print("Esse número já foi adicionado. Digite um valor diferente!")

print("\nPrograma encerrado!")
print(f"Sua lista final de números únicos: {sorted(valores)}", )


