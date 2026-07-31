x = int(input("Que numero deseja multiplicar? "))
i = 0
m = 0

for i in range(1, 11):
    m = i * x
    print(f"{i} x {x} = {m}")