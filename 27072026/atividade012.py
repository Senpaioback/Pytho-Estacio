soma_idade = 0
maior_idade_homem = 0
nome_velho = ''
tot_mulher_20 = 0

for p in range(1, 5):
    print(f'----- {p}ª PESSOA -----')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()
    
    # 1. Soma as idades para calcular a média no final
    soma_idade += idade
    
    # 2. Verifica o homem mais velho
    if p == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
        
    # 3. Conta mulheres com menos de 20 anos
    if sexo in 'Ff' and idade < 20:
        tot_mulher_20 += 1

media_idade = soma_idade / 4

print(f'\nA média de idade do grupo é de {media_idade:.1f} anos.')
if nome_velho != '':
    print(f'O homem mais velho tem {maior_idade_homem} anos e se chama {nome_velho}.')
else:
    print('Não há homens no grupo.')
print(f'Ao todo são {tot_mulher_20} mulheres com menos de 20 anos.')