import random

i = random.randint(0,10)
f = random.randint(0,10)
print(f'o primeiro número é: {i}\no segundo número é: {f}')

while True:
    p = int(input('qual o valor da multiplicação desses dois números?\n'))
    if p == i * f:
        print('ACERTOU!')
        break
    else:
        print('ERROU!')
        c = int(input(f'[1] Continuar tentando\n[2] Sair\nEscolha uma opção: '))
        if c == 1:
            continue
        elif c == 2:
            print('Valeu a tentativa!')
            break
        else:
            print('Digite uma opção válida')
            continue
