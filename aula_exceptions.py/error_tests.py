def main():
    x = get_int()
    print(f"x is {x}")

def get_int():

#define o loop do programa ate que o usuario escreva um numero
    while True:

        try:
            return int(input("what's x? "))

        except ValueError:
            print("x is not an integer")
    


main()