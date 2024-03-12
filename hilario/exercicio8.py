def main():
    d = atual(input("Quanto você ganha? "))
    p= porcentagem(input("Quantos porcento a mais? "))
    aumento = d * p
    print(f"Seu novo salário é ${aumento:.2f}")


def atual(d):

    d = float(d.strip("$"))
    return d

def porcentagem(p):

    p = float(p.strip("%")) /100
    return p

main()