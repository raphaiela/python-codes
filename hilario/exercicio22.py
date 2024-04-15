soma = 0
while True:
    quest = int(input('Digite um número: '))
    if quest != 0:
        soma += quest
        continue
    
    elif quest == 0:
        print(soma)
        break
