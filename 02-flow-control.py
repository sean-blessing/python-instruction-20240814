# p. 43 Flow control

# p. 45 if-else
# p. 47 white space
# driver_age = 15
# eligible_to_drive = False

# if driver_age >= 16:
#     eligible_to_drive = True

# else:
#     eligible_to_drive = False

# traffic light
# if light is red - stop
# else if light is green - go
# else if light is yellow - slow down
# else wrong light color
# light_color = input("What is the light color? ").lower()

# if light_color == "red":
#     print("Stop!")
# elif light_color == "green":
#     print("Go!")
# elif light_color == "yellow":
#     print("Slow down.")
# else:
#     print("invalid color")

# p. 48 conditional expression
# driver_age = 15
# eligible_to_drive = True if driver_age >= 16 else False
# print(f'eligible_to_drive: {eligible_to_drive}')

# p. 49 relational operators
# a = 55

# if a == 50:
#     print(50)
# elif a != 50:
#     print(50)
# elif a <= 50:
#     print("<=50")
# elif a < 50:
#     print("<50")
# elif a >= 50:
#     print(">=50")
# elif a > 50:
#     print(">50")

# p. 51 boolean operators
print(12 and 5)

# p. 53 while loops

# while True:
#     light_color = input("What is the light color? ").lower()
#     if light_color == "red":
#         print("Stop!")
#     elif light_color == "green":
#         print("Go!")
#     elif light_color == "yellow":
#         print("Slow down.")
#     else:
#         print("invalid color")
#         break

# p. 54 loop control - break/continue
# while True:
#     number = int(input("Enter the number 10."))
#     if number < 10:
#         print("number is less than 10")
#         continue
#     elif number > 10:
#         print("number is greater than 10.")
#         continue
#     elif number ==10:
#         print("10")
#         break
#     print("end of while loop")
# print('bye')

# final while loop example
menu_option = ''

# print a menu and display the option selected, exit when they enter 'exit'
# (Instead of using "while True")
while menu_option != "exit":
    menu_option = input("""
        Choose your option: 
        list - list items
        add - add an item
        exit - exit application
        """)
    if menu_option == "list":
        print("you chose list")
    elif menu_option == "add":
        print("you chose add")
    elif menu_option == "exit":
        print("you chose exit")
    else:
        print("invalid option")
print("bye")