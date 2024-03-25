while True:
    l1 = int(input('Qual o primeiro lado? '))
    l2 = int(input('Qual o segundo lado? '))
    l3 = int(input('Qual o terceiro lado? '))

    if l1 == l2 == l3:
        print('Triangulo equilatero.')
        break
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('Triangulo isoceles.')
        breakpoint
    elif l1 != l2 != l3:
        if l1 > l2 + l3 or l2 > l1 + l3 or l3 > l1 + l2:
            print('Nao e triangulo.')
            continue
        else:
            print('Triangulo escaleno.')
            break
