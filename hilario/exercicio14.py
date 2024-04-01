vogais = ["A", "E", "I", "O", "U"]
enter = str(input("Digite uma letra: ")).upper().strip()
if enter in vogais:
    print(f"{enter} é uma vogal!")
elif enter.isdigit():
    print("Digite apenas letras!")
else:
    print(f"{enter} é uma consoante!")
