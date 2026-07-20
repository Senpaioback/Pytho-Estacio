dias = int(input("Quantas dias quer alugar: "))
km = float(input("Quantos km vai rodar: "))
pago = (dias * 60) + (km * 0.15)
print(f"Total: {pago}")