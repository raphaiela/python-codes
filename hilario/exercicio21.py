while True:
    print('[1] Exibir nova tabuada\n[2] Encerrar')
    esc = int(input('Qual opção você deseja? '))

    if esc == 1:
        num = int(input('Digite o número: '))
        tab = 0
        while tab < 11:
            print(f'{num} x {tab} =', num * tab)
            tab = tab + 1
            continue
    else:
        break
