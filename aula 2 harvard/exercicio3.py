def main():
    
    x = int(input("what's x? "))


    def is_even (n):

        return True if n % 2 == 0 else False
    
    if is_even(x) is True:
        print("x is even")
    else:
         print("x is odd")

main() 
