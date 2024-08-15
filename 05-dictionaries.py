# # p. 113 - Creating dictionaries

# # storing states by key (abbreviation), value (state name)
# # 'OH' - 'Ohio', 'IN' - 'Indiana'
# states = {
#     'OH': 'Ohio',
#     'IN': 'Indiana',
#     'CO': 'Colorado',
#     'KY': 'Kentucky'
# }

# days_of_week = dict(Mon='Monday', Tues='Tuesday', Wed='Wednesday',
#                     Thurs='Thursday', Fri='Friday', Sat='Saturday', Sun='Sunday')

# # accessing values of a dictionary:
# print(f"OH is {states['OH']}")
# print(f'Mon is {days_of_week.get('Mon')}')

# # add values to a dictionary
# states['TS'] = 'Tennessee'
# print(f'states: {states}')

# # remove an entry
# state_removed = states.pop('TS')
# print(f'{state_removed} was removed')
# print(f'states: {states}')

# # p. 119 iterating over a dictionary
# print("====== iterating over dictionary =========")
# print(f'keys: {states.keys()}')
# print("-"*10)
# print(f'values: {states.values()}')
# print("-"*10)
# print(f'items: {states.items()}')
# print("-"*10)

# # p. 120 unpacking, sorting
# print(" unpack key values:")
# for abbr, name in states.items():
#     print(f'key: {abbr}, value: {name}')
# print("="*30)
# print("** sorted")
# print(" unpack key values:")
# for abbr, name in sorted(states.items()):
#     print(f'key: {abbr}, value: {name}')
# print("="*30)

# p. 121 reading file into dictionary

# from pprint import pprint

# knight_info = {}  # create empty dict

# with open("./files/knights.txt") as knights_in:
#     for line in knights_in:
#         name, title, color, quest, comment = line.rstrip('\n\r').split(":")
#         knight_info[name] = title, color, quest, comment  # create new dict element with name as key and a tuple of the other fields as the value

# print("======")
# print(knight_info)
# print("===pretty print===")
# pprint(knight_info)
# print("======")
# print()

# for name, info in knight_info.items():
#     print(info[0], name)

# print()
# print(knight_info['Robin'][2])

# p. 128 sets
set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set2 = {6, 7, 8, 9, 10, 11, 12, 13, 14, 15}

print("=== set comparisons ====")
print(f"set1: {set1}")
print(f"set2: {set2}")
print(f"intersection &: {set1 & set2}")
print(f"symmetric difference ^: {set1 ^ set2}")
print(f"union |: {set1 | set2}")
print(f"difference set1 - set2: {set1 - set2}")
print(f"difference set2 - set1: {set2 - set1}")