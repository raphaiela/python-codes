n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))

d = {n1: "primeiro", n2:"segundo", n3: "terceiro"}
l = [n1, n2, n3]

for i in l:
        
    if i % 2 == 0:
        print(f"{d[i]} numero é par.")
    else:
        print(f"{d[i]} numero é 1ímpar.")
