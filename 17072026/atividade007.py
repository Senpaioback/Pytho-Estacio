largura = float(input("Quanto de largura tem sua parede? "))
altura = float(input("Quanto de altura tem sua parede? "))

area = largura * altura
total_de_litro = area / 2

print(f"Largura: {largura}m\n Altura: {altura}m\n Area: {area}m²\n total de tinta para pintar a parede: {total_de_litro}L")