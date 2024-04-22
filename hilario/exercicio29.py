p = 0
im = 0
for i in range(10):
    n = int(input(f'Digite o {i+1} número: '))
    if n % 2 == 0:
        p += n
    elif n % 2 != 0:
        im += n
print(f'A soma dos números pares é: {p}\nA soma dos números ímpares é: {im}')