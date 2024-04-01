nota1 = float(input("Qual foi sua nota 1? "))
nota2 = float(input("Qual foi sua nota 2? "))
aulas = int((input("Quantas aulas você teve? ")))
faltas = int(input("Quantas faltas você teve? "))

if (nota1 + nota2) / 2 >= 7 and (aulas - faltas) * 100 / aulas >= 75:
    print("Aprovado!")
else:
    print("Reprovado!")
