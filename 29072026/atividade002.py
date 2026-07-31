import random

numero = random.randint(1, 10)
numero_player = int(input("Digite um número: "))
tentativas = 1  # Iniciamos o contador na 1ª tentativa

# O loop continua enquanto o jogador não acertar
while numero_player != numero:
    print("Você errou!")
    tentativas += 1  # Somamos +1 a cada erro/tentativa
    numero_player = int(input("Tente novamente. Digite um número: "))

print(f"Você acertou! O número era {numero}. Você precisou de {tentativas} tentativa(s).")