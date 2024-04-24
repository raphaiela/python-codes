def telefone():
    tel = input("Digite seu número de telefone: ")
    print(tel)
    if tel == 9:
        print("Digite o DDD, por favor.")
        return True
    elif tel == 11:
        print("Telefone enviado com sucesso!")
        return False
i = str(input("Olá, como vai? Poderia inserir os valores solicitados? \n---> "))
if i == "sim":
    telefone()
else:
    print("Obrigado!")

