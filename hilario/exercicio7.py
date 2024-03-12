d = int(input("Quantos dias? "))
h = int(input("Quantas horas? "))
m = int(input("Quantos minutos? "))
s = int(input("Quantos segundos? "))

calculo = (d * 86.400) + (h * 3600) + (m * 60) + s

print(f"São {calculo} segundos")