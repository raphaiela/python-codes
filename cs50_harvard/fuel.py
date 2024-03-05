while True:
    try:
        f = str(input("Fraction: "))

        x, y = map(int, f.split("/"))

        f = x/y * 100

        if f <= 1:
            print("E")
            break
        elif f >= 99:
            print("F")
            break
        else:
            f = int(f)
            print(f"{f}%")
            break

    except ValueError:
        print("Valor digitado não é valido")
        continue
    except ZeroDivisionError:
        print("Divisão por 0 não é possível")
        continue
