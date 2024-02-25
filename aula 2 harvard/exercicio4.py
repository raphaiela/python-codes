name = input("Qual o seu nome? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("sua casa eh Slytherin")
    case _:
        print("Who???")