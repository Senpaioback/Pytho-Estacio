num = [1, 3, 5, 7]
num[2] = 9
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)
num.pop(2)
print(num)
print(f"Essa lista tem {len(num)} elementos")