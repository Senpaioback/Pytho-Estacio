tabela_brasileirao = (
    "Palmeiras",
    "Flamengo",
    "Athletico-PR",
    "Fluminense",
    "Cruzeiro",
    "Bahia",
    "Bragantino",
    "Atlético-MG",
    "Corinthians",
    "Coritiba",
    "Botafogo",
    "EC Vitória",
    "São Paulo",
    "Santos",
    "Grêmio",
    "Mirassol",
    "Internacional",
    "Remo",
    "Vasco da Gama",
    "Chapecoense",
)

print(f"Lista dos Times do Brasileirão: {tabela_brasileirao}")
print(f"Os 5 primeiros são {tabela_brasileirao[0:5]}")
print(f"Os 4 ultimos são {tabela_brasileirao[-4:]}")
organizar = sorted(tabela_brasileirao)
print(f"Times em ordem alfabetica {organizar}")
posicao = tabela_brasileirao.index("Chapecoense")
print(f"chapecoense esta na posição {posicao}º")
