distancia = float(input("Quantos KM pretende rodar? "))

km_200km = 0.50
km_amais200km = 0.45

if distancia <= 200:
    s1 = distancia * km_200km
    print(f"Sua distancia percorrida será {distancia}Km.\nO preço final: R$ {s1}")
else:
    s2 = distancia * km_amais200km
    print(f"Sua distancia percorrida será {distancia}Km.\nO preço final: R$ {s2}")
