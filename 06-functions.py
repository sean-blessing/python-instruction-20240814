# p. 132 Functions
# p. 134 function basics

# function w/ no parameters
# def print_hello():
#     print('Hello!')

# call the function
# print_hello()

# function w/ no parameters that returns a value
# def print_hello_2():
#     return "Hello!!"

# print(print_hello_2())

# print_hello()

# function that takes 1 parameter w/ no return
# def print_welcome_msg(name):
#     #print("Hello "+name)
#     print(f"Hello {name}")
# print_welcome_msg("Steven")
# print(name) # Note: can't access name - only exists inside function
# print_welcome_msg()

# demo of variable declaration and access after block
# while True:
#     xyz = "xyz"
#     print(xyz)
#     break

# print(f' can i access xyz here?: {xyz}')

# function that takes 2 parameters and returns a value
# def add_2_nums(num1, num2):
#     return num1 + num2

# def add_3_nums(num1, num2, num3):
#     return num1 + num2 + num3


# print(f'Add 1 and 2: {add_2_nums(1, 2)}')
# print(f'Add 10 and 25: {add_2_nums(10, 25)}')
# print(f'Add 88 and 33: {add_2_nums(88, 33)}')
# print(f'Add 1, 5, 8: {add_3_nums(1, 5, 8)}')

# # add 3 numbers?
# print(f'Add 1 and 2 and 3: {add_3_nums(1, 2, 3)}')

# # declare add function that accepts a variable number of ints
# def add(nums):
#     sum = 0
#     for num in nums:
#         sum = sum + num
#         #sum += num
#     return sum

# print(f'add 1, 5, 9: {add([1, 5, 9])}')
# print(f'add 2, 50: {add([2, 50])}')
# print(f'add 33, 77, 92, 11: {add([33, 77, 92, 11])}')


# p. 136 - function w/ a parameter w/ default value
# def print_welcome_message(name='World'):
#     print(f"Hello {name}!!!!")

# print_welcome_message("Sarah")
# print_welcome_message()
# print_welcome_message(name="Raji")

# print("a", end=" ")
# print("b", end="-")
# print("c", end="")
# print("d")
# print("e", end='')
# print("f")

# optional parameter

# named parameters
# def named_parameter_function(**named_args):
#     print("named_parameters_function()")
#     for name in named_args:
#         print(f'{name}: {named_args[name]}', end=', ')
#     print()

# named_parameter_function(name="Sreejith", day="Friday", date='20240816')
# named_parameter_function(name="Sreejith", day="Friday", date='20240816', month='August')

# p. 142 Scope

x = 42  # global variable


def function_a():
    # global variables are NOT recommended
    global i
    i = 255
    y = 5  # local variable to function_a(), or nonlocal to function_b()

    def function_b():
        z = 32  # local variable
        print("function_b(): z is", z)  # local scope
        print("function_b(): y is", y)  # nested (nonlocal) scope
        print("function_b(): x is", x)  # global scope
        print("function_b(): type(x) is", type(x))  # builtin scope

    return function_b


f = function_a()  # calling function_a, which returns function_b
f()  # calling function_b
# calls made outside of functions
print(f'x: {x}')
# print(f'y: {y}')
# print(f'z: {z}')
print(i)

# p. 147
# use a module
#import samplelib as samp
from my_modules.samplelib import hello_from_samplelib, print_separator

#samplelib.hello_from_samplelib()
#samp.hello_from_samplelib()
hello_from_samplelib()
print_separator(50)
hello_from_samplelib()
print_separator(25)

import pprint

pprint.pprint("Hello")