salario = float(input("Digite o seu salario: "))

if salario <= 1.250:
    abaixo = 15
    aumento = (salario / abaixo) + salario
    print(f"Salario Final R${aumento}")
else:
    acima = 10
    aumento = (salario / 10) + salario
    print(f"Salario final: R${aumento}")

