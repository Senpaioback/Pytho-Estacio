# Nome com todas as letras mauiscula, nome com todas minuscula, quantas letra tem sem considerar os espaços, quantas letras tem sem considerar o primeiro nome

nome = "Pedro Lemes Ramos"
print(nome.upper())
print(nome.lower())
tamanho = len(nome) - nome.count(" ")
print(tamanho)
print(len(nome[6:16]))