while True:
    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite um número: "))
    sinal = str(input("Digite a operação: "))

    if sinal.isdigit() or sinal.isalpha():
        continue 
    else:
        if sinal == "+":
            print(num1 + num2)
            break
        elif sinal == "-":
            print(num1 - num2)
            break
        elif sinal == "/":
            print(num1 / num2)
            break
        elif sinal == "*":
            print(num1 * num2)
            break
