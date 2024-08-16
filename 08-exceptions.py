# chapter 8

def get_int(prompt):
    #wrap in try-except to catch the error
    number = 0
    while True:
        try:
            number = int(input(prompt))
            break
        except ValueError as err:
            print("Error - invalid whole number. Try again.")
    return number

nbr1 = get_int("Enter a whole number: ")

print(f'You entered {nbr1}')