# a funcao main vai rodar o codigo
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# a funcao is_valid vai checar os requisitos para ser valido
def is_valid(s):

# REQUISITOS:

    # conter no minimo 2 e no maximo 6 caracteres
    if len(s) < 2 or len(s) > 6:
        return False

    # proibido numeros no comeco
    # letras no comeco
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False

    # verifica se o primeiro numero escrito eh 0
    i = 0
    # o elemento i representa cada caractere da lista s
    while i < len(s):

        # essa condicao checa o primeiro numero
        if s[i].isalpha() == False:
            # essa subcondicao checa se o primeiro numero eh 0 e retorna falso
            if s[i] == "0":
                return False
            # senao encerra a checagem do primeiro numero
            else:
                break
        # adiciona uma posicao e retorna o loop while (para checar todos os elementos escritos)
        i += 1

    # proibido sinais de pontuacao e espacos
    for x in s:
        # se o elemento pertencer a um dos elementos da lista x, retorna falso
        if x in [".", " ", "!", "?"]:
            return False

    return True

main()
