import functions

inp = int(input("Olá, como vai? Poderia inserir os valores solicitados? \n[1] Sim\n[2] Não\n---> "))
if inp == 1:
    telefone()
    cpf()
else:
    print("Obrigado!")