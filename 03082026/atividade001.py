n = cont = 0
while True: 
    n = int(input("Digite um numero: (999 para sair do programa)"))
    if n != 999:
        print("Voce saiu do programa")
        break
    cont += n
print(cont)