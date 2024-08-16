import random
min_val = 1
max_val = 25

print("Welcome to the guess the number game!")
print("="*40+"\n")

# start a game
choice = "y"

def validate_int_range(prompt):
    valid_entry = False
    number = 0
    
    while valid_entry != True:
        try:
            number = int(input(prompt))
            if number < min_val or number > max_val:
                print(f"Entry must be within range {min_val} to {max_val}")
            else:
                valid_entry = True
        except:
            print("Invalid entry. Please try again.")
    return number
    
while choice == "y":
    print(f"I'm thinking of a number between {min_val} and {max_val}. Try to guess it.")

    count = 0
    guess = 0
    the_number = random.randint(min_val, max_val+1)
    print(f"*** Cheat: the number is {the_number}. ***")
    print()

    while guess != the_number:
        guess = validate_int_range("What's your guess? ")
        count+=1
        diff = guess - the_number
        # diff < -10: way too low
        # diff < 0: too low
        # diff > 10: way too high
        # diff > 0: too high
        # else: winner!
        if diff < -10:
            print("Way too low!")
        elif diff < 0:
            print("Too low.")
        elif diff > 10:
            print("Way too high!")
        elif diff > 0:
            print("Too high.")
        else:
            print(f'You guessed it in {count} tries.')
            if count <=3:
                print("Great work! You are a mathematical wizard")
            elif count <= 7:
                print("Not too bad! You've got some potential")
            else:
                print("What took you so long? Maybe you should take some lessons.")
    # end game
    while True:
        choice = input("Play again (y/n)? ").lower()
        if choice != "y" and choice != "n":
            print("Invalid choice. Try again.")
        else:
            break
        

print("Bye. Thanks for playing!")