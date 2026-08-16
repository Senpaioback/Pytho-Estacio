contagem = (
    "zero", "um", "dois", "três", "quatro",
    "cinco", "seis", "sete", "oito", "nove",
    "dez", "onze", "doze", "treze", "quatorze",
    "quinze", "dezesseis", "dezessete", "dezoito", "dezenove",
    "vinte"
)

# Loop para continuar pedindo até receber um número válido
for _ in iter(int, 1):
    escolha = int(input("Digite um número entre 0 e 20: "))
    
    # Valida se o número está dentro do intervalo
    if 0 <= escolha <= 20:
        # Percorre a tupla pegando a posição (pos) e o texto (extenso)
        for pos, extenso in enumerate(contagem):
            if pos == escolha:
                print(f"Você digitou o número {extenso}.")
                break
        break
    else:
        print("Tente novamente. ", end="")

print("Fim do programa.")  
    