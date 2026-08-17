palavras = ("morango", "vida", "minecraft", "games", "gameplay", "vasco", "pedro", "carro", "morder")

for p in palavras:
    print(f"\nA {p.upper()} tem ", end=" ")
    for letra in p: 
        if letra.lower() in 'aeiou':
            print(letra, end=' ')