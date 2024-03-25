a = int(input('Digite o primeiro angulo: '))
b = int(input('Digite o segundo angulo: '))
c = int(input('Digite o terceiro angulo: '))

if a + b + c > 180 or a <= 0 or b <= 0 or c <= 0:
    print('isso nao e um triangulo.')
else:
    if a < 90 and b < 90 and c < 90:
        print('triangulo acutangulo!')
    elif a == 90 or b == 90 or c == 90:
        print('triangulo retangulo!') 
    elif a > 90 or b > 90 or c > 90:
        print('triangulo obrtusangulo!')
