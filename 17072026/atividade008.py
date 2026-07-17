preco = float(input("Preço do produto: R$"))

desconto = ( 5 / 100) * preco
total = preco - desconto

print(f"Desconto de 5%, o preço final ficou: R$ {total}")