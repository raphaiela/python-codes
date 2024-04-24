def telefone():
    while True:
        tel = input("Digite seu número de telefone: \n")
        if len(tel) != 11:
            print("Digite o DDD, por favor. O número de telefone deve conter 9 números.")
            continue
        else:
            print("Telefone armazenado com sucesso!")
            break

def cpf():
    while True:
        cpf = int(input("Digite o número de seu CPF: \n"))
        if len(cpf) != 11:
            print("O número de CPF deve conter 11 digitos.")
            continue
        else:
            print("Número de CPF arquivado com sucesso!")
            break


