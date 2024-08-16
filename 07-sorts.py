#162 Chapter 7 sorting
"""Basic sorting example"""

fruits = ["pomegranate", "cherry", "apricot", "date", "Apple", "lemon", "Kiwi",
         "ORANGE", "lime", "Watermelon", "guava", "papaya", "FIG", "pear", "banana",
         "Tamarind", "persimmon", "elderberry", "peach", "BLUEberry", "lychee",
         "grape"]

# print(f'fruits raw: {fruits}')
# fruits.sort()
# print(f'fruits sorted: {fruits}')

# sorted_fruit = sorted(fruits)  # sorted() returns a list
# print("="*20)
# print(sorted_fruit)

# #p. 165 custom sort keys
# # key=str.lower is built in to Python
# sorted_fruit = sorted(fruits, key=str.lower)  # sorted() returns a list
# print(f'fruits sorted - using key=str.lower: {sorted_fruit}')

# # custom sort
# def ignore_case(item):
#     return item.lower()

# print("="*20)
# print(f'fruits unsorted: {fruits}')
# print("="*20)
# sorted_fruits_2 = sorted(fruits, key=ignore_case)
# print(f'fruits sorted 2: {sorted_fruits_2}')

# p. 168
# books = [
#     "A Study in Scarlet",
#     "The Sign of the Four",
#     "The Hound of the Baskervilles",
#     "The Valley of Fear",
#     "The Adventures of Sherlock Holmes",
#     "The Memoirs of Sherlock Holmes",
#     "The Return of Sherlock Holmes",
#     "His Last Bow",
#     "The Case-Book of Sherlock Holmes",
# ]

# def print_books(book_list):
#     print("== books ==")
#     for book in book_list:
#         print(book)
#     print("="*20)

# print_books(books)

# sorted_books = sorted(books, key=str.lower)
# print_books(sorted_books)

# # define a custom sort that removes "A" "An" and "The"
# def strip_article(title):
#     title = title.lower()
#     for article in 'a ', 'an ', 'the ':
#         if title.startswith(article):
#             title = title.removeprefix(article)
#             break
#     return title

# sorted_books = sorted(books, key=strip_article)
# print_books(sorted_books)

# p. 171 lambda sort
# print(f'fruits: {fruits}')
# sf_1 = sorted(fruits, key=lambda e: e.lower() )
# print("ignoring case:")
# print(' '.join(sf_1))
# print()

# p. 174 computer people sort
computer_people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

print(f'computer_people: {computer_people}')
# sort this list based on various criteria
scp_1 = sorted(computer_people)
print(f'scp_1: {scp_1}')

# sort by last name
scp_2 = sorted(computer_people, key=lambda e: e[1])
print(f'scp_2: {scp_2}')

# sort by company (3rd field in the tuple)
scp_3 = sorted(computer_people, key=lambda e: e[2])
print(f'scp_3: {scp_3}')

# sort by bdate (4th field in the tuple)
scp_4 = sorted(computer_people, key=lambda e: e[3])
print(f'scp_4: {scp_4}')

def by_last_first(item):
    return item[1], item[0]

# sort by last, first
scp_5 = sorted(computer_people, key=by_last_first)
print(f'scp_5: {scp_5}')
