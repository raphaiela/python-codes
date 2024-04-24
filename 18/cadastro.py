from functions import telefone, cpf

inp = str(input("Olá, como vai? Poderia inserir os valores solicitados? \n---> "))
if inp == "sim":
    telefone()
    cpf()
else:
    print("Obrigado!")