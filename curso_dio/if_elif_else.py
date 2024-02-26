opção = int(input("Informe uma opção:\n [1] Sacar \n [2] Extrato\n "))

if opção == 1:
    valor = float(input("Informe a quantia para saque: "))

elif opção == 2:
    print("Exibindo o extrato... ")

else:
    print("Opção inválida. ")