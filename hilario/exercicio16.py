while True:
    print(" [1] Homem\n [2] Mulher\n")
    sexo = int(input("Qual o seu sexo? "))
    h = float(input("Qual a sua altura? "))

    if sexo == 1:
        ideal = (72.7 * h) - 58
        print(f"Seu peso ideal é {round(ideal)}")
        break
    elif sexo == 2:
        ideal = (62.1 * h) - 44.7
        print(f"Seu peso ideal é {round(ideal)}")
        break
    else:
        print("Escolha uma opção válida!")
        continue
