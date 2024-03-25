a = int(input('Digite A: '))
b = int(input('Digite B: '))
c = int(input('Digite C: '))
d = int(input('Digite D: '))

if b > c and d > a and (c + d) > (a + b) and c > 0 and d > 0 and a % 2 == 0:
    print('valores aceitos!')
else:
    print('valores não aceitos')
