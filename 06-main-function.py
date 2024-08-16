# reference: https://www.geeksforgeeks.org/python-main-function/

def main():
    print("Welcome to the main function app!")
    name = input("What is your name? ")
    print_hello(name)
    print("Let's add some numbers...")
    int1 = get_int("Enter first number: ")
    int2 = get_int("Enter second number: ")
    print_sep(30)
    print(f'Sum of {int1} and {int2} is {add_two(int1, int2)}')
    
    print("Bye")
    
def print_hello(name='World'):
    print(f"Hello {name}")

def add_two(nbr1, nbr2):
    return nbr1 + nbr2

def get_int(prompt):
    return int(input(prompt))

def print_sep(nbr):
    print("="*nbr)

if __name__=="__main__":
    main()
