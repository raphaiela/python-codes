def main():
    x = get_int("what's x? ")
    print(f"x is {x}")

def get_int(prompt):

#define o loop do programa ate que o usuario escreva um numero
    while True:

        try:
            return int(input(prompt))

        except ValueError:
            print("x is not an integer")
    


main()