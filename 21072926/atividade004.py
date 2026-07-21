multa = 7.00
carro = 90
max_da_estrada = 80
calculo_d_multa = (carro - max_da_estrada) * multa

if carro > max_da_estrada:
    print(f"Voce recebeu uma multa de: {calculo_d_multa} por ultrapassar os 80km/h")
else:
    print("Parabens, continue abaixo do limite de velocidade, sua vida é bem mais importante")