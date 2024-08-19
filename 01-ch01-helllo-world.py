# p. 7 Chapter 1

print('hello world!!!!!!!!!')
print("hello world, again.")
print("Hello Mr. Mc'Neally")

# p. 8 variables
first_name = "Bob"
last_name = "Marley"

print(first_name)
print(last_name)

print(first_name+last_name)
print(first_name + ' ' + last_name)
print(f'{first_name:20s} {last_name}')

# this is a comment!
# this is another comment!
"""
Hello this
is a
multi
line
comment
"""

# p. 13 new line \n, tab \t
print("This is one line\nThis is another line.")
print("Beginning of string\tAfter tab")

# p.14 triple-delimited string
print("""James Earl "Jimmy" Carter""")
print("""
      This is a song
      It's a really great song
      It has several lines
      """)
query = '''
from contacts
where zip = '90210'
order by lname
'''
print(f'query = {query}')

# p. 15 raw strings
folder_name = r'c:\repos\python-instruction'
print(folder_name)

# p. 16 unicode characters
# print the copyright symbol
print("\u00A9")

# p. 19 string operators
lower_case_string = "hello how are you"
print(f'lower_case_string: {lower_case_string}')
print(f'upper case: {lower_case_string.upper()}')
print(f'lower_case_string: {lower_case_string}')
print(f'title: {lower_case_string.title()}')

# p. 21 string methods
print(f'capitalize: {lower_case_string.capitalize()}')

# p. 24 numeric literals
price = 24.99
quantity = 5
print(f'price * quantity = {price * quantity}')
total_price = 500.50
print(f'price divided by 2: {total_price / 2}')

a = 33
print(type(a))
b = a / 2
print(f'b: {b}')
print(type(b))
print(f'remainder: {a % 2}')

# p. 25
a = 5
b = 10
c = 20.22

print("a, b, c: ", a, b, c)

# p. 27 exponents - 2 to the 3rd power
print(2 ** 3)
print(pow(2,3))

# p. 30
print("Hello, ",end='')
print("Bob")

# p. 34
result = 32.128935
print(f'result = {result}')
print(f'result rounded to two decimal places = {result:.2f}')

