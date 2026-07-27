altura = float(input("Qual sua altura: "))
peso = float(input("Qual seu peso: "))

IMC = peso / (altura * altura)

if IMC <= 18.5:
    print("Abaixo do peso")
elif IMC > 18.5 and IMC <= 25:
    print("Ideal")
elif IMC > 25 and IMC <= 30:
    print("Sobrepeso")
elif IMC > 30 and IMC <= 40:
    print("Obesidade")
else:
    print("Obesidade Morbida")