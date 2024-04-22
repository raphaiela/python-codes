aluno = int(input('Quantas médias deseja calcular? '))
if aluno == 1:
    print('Informe as notas N1 e N2 desse aluno:')
    n1 = float(input())
    n2 = float(input())
    print(f'A média desse aluno foi {(n1+n2)/2}')
else:
    for i in range(aluno):
        print(f'Informe as notas N1 e N2 do aluno {i+1}')
        n1 = float(input())
        n2 = float(input())
        print(f'A média do aluno {i+1} foi {(n1+n2)/2}')
