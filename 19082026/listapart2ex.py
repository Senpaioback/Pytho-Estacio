teste = list()
teste.append("Pedro")
teste.append(40)

galera = list()  # Uso correto com parênteses
galera.append(teste[:])  # teste[:] cria uma cópia dos valores

teste[0] = "maria"
teste[1] = 22
galera.append(teste[:])  # Outra cópia independente

print(galera)