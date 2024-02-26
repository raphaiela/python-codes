opção = int(input("Informe uma opção:\n [1] Conta normal \n [2] Conta universitária\n "))

conta_normal = saldo = 1000
conta_universitaria = saldo1 = 1000
cheque_especial = 200

saque = int(input("Qual o valor do saque? "))

if opção == 1:
    if saldo >= saque:
        print("Realizando saque... ")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial! ")
    else:
        print("Saldo insuficiente! ")
elif opção == 2:
    if saldo1 >= saque:
        print("Realizando saque... ")
    else:
        print("Saldo insuficiente! ")
