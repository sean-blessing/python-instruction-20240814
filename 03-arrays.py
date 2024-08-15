# p. 58 Array Types

# p. 60 basic arrays
fruits = ['apple', 'cherry', 'orange', 'kiwi', 'banana', 'pear', 'fig'] # list
name = "Eric Idle"  # str
knight = 'King', 'Arthur', 'Britain'  # tuple
data = b"abcde"   # bytes

# print(fruits[6])  # print 4th element of fruits
# print(name[5])  # print 3rd letter of name
# print(knight[1])  # print 2nd element of knight
# print(data[4])  # print 5th element of data


# p. 61 lists
# p. 63 using_lists.py - examples
# cities = ['Cincinnati', 'Columbus', 'Toledo']
# print(f'cities: {cities}')
# print(cities[0])
# cities.append('Cleveland')
# print(cities)
# cities.remove('Toledo')
# print(cities)
# cities[1] = 'Akron'
# print(cities)
# cities.insert(1,'Dayton')
# print(cities)
# new_cities = ['Sandusky', 'Put-In Bay']
# cities.extend(new_cities)
# print(cities)

# print(f'pop cities[2]: {cities.pop(2)}')
# print(cities)

# print(f'pop cities: {cities.pop()}')
# print(cities)

# p. 65 indexing and slicing
# p. 67 indexing_and_slicing.py - examples
pythons = ["Idle", "Cleese", "Chapman", "Gilliam", "Palin", "Jones"]
characters = "Roger", "Old Woman", "Prince Herbert", "Brother Maynard"
phrase = "She turned me into a newt"

# print(f'pythons: {pythons}')
# print(f'1st element: {pythons[0]}')
# print(f'6th element: {pythons[5]}')
# print(f'first 3 elements: {pythons[0:3]}')
# print(f'3rd element thru end: {pythons[2:]}')
# print(f'first 3 elements: {pythons[:3]}')
# print(f'2nd thru next-to-last element: {pythons[1:-1]}')
# print(f'first 3 elements: {pythons[0:3]}')
# print(f'every other element starting with first: {pythons[0::2]}')
# print(f'every other element starting with second: {pythons[1::2]}')

# print(f'phrase: {phrase}')
# print(f'phrase[0]: {phrase[0]}')
# print(f'phrase[-1]: {phrase[-1]}')
# print(f'phrase[2:8]: {phrase[2:8]}')

# p. 69 iterating through a sequence
# my_list = ["Idle", "Cleese", "Chapman", "Gilliam", "Palin", "Jones"]
# my_tuple = "Roger", "Old Woman", "Prince Herbert", "Brother Maynard"
# my_str = "She turned me into a newt"

# p. 72 tuples
# create a tuple of Movie information
# Movie: title, year, rating, director
movie = "Star Wars", 1977, "PG", "George Lucas"
print(f'movie: {movie}')
# things = [1, "two", 3.3]
# iterate over elements of a tuple
for element in movie:
    print(f'element: {element}')

numbers = [1, 7, 2, 8, 5]
for nbr in numbers:
    print(f'number: {nbr}')
    
name = "Eric Idle"
for char in name:
    print(f'char: {char}')

# p. 74 iterable unpacking
# p. 75 iterable_unpacking.py - examples
values = ['a', 'b', 'c']

# x, y, z = values  # unpack values (which is an iterable) into individual variables

# print(x, y, z)
# print()

# people = [
#     ('Bill', 'Gates', 'Microsoft'),
#     ('Steve', 'Jobs', 'Apple'),
#     ('Paul', 'Allen', 'Microsoft'),
#     ('Larry', 'Ellison', 'Oracle'),
#     ('Mark', 'Zuckerberg', 'Facebook'),
#     ('Sergey', 'Brin', 'Google'),
#     ('Larry', 'Page', 'Google'),
#     ('Linux', 'Torvalds', 'Linux'),
# ]

# for row in people:
#     first_name, last_name, _ = row  # unpack row into variables
#     print(first_name, last_name)
# print()

# for first_name, last_name, _ in people:  # a for loop unpacks if there is more than one variable
#     print(first_name, last_name)
# print()

# p. 77 nested sequences
people = [
    ('Melinda', 'Gates', 'Gates Foundation'),
    ('Steve', 'Jobs', 'Apple'),
    ('Larry', 'Wall', 'Perl'),
    ('Paul', 'Allen', 'Microsoft'),
    ('Larry', 'Ellison', 'Oracle'),
    ('Bill', 'Gates', 'Microsoft'),
    ('Mark', 'Zuckerberg', 'Facebook'),
    ('Sergey', 'Brin', 'Google'),
    ('Larry', 'Page', 'Google'),
    ('Linus', 'Torvalds', 'Linux'),
]
# p. 81 functions for all sequences

# p. 83 iterators
# p. 86 iterators.py
# p. 87 using_ranges.py

# p. 88 list comprehension
fruits = ['watermelon', 'apple', 'mango', 'kiwi', 'apricot', 'lemon', 'guava']

