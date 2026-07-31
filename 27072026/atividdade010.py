from datetime import date

# Pega o ano atual do sistema
ano_atual = date.today().year

# Contadores
tot_maior = 0
tot_menor = 0

# Laço para ler o ano de nascimento de 7 pessoas
for pess in range(1, 8):
    nasc = int(input(f'Em que ano a {pess}ª pessoa nasceu? '))
    idade = ano_atual - nasc
    
    if idade >= 21:
        tot_maior += 1
    else:
        tot_menor += 1

# Exibição dos resultados
print(f'\nAo todo tivemos {tot_maior} pessoas maiores de idade.')
print(f'E também tivemos {tot_menor} pessoas menores de idade.')

