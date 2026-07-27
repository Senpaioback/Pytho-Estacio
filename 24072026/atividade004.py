ano_nascimento = int(input("Digite seu ano de nascimento: "))
resultado =  2026 - ano_nascimento

if resultado < 18:
    print(f"Voce ainda vai se alista\n falta {18 - resultado} anos para seu alistamento")
elif resultado == 18:

    print(f"Esta na hora de se alistar.")
else:
    print(f"Ja passou do tempo\n Se passou {resultado - 18} anos do seu alistamento")