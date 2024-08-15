# p. 113 - Creating dictionaries

# storing states by key (abbreviation), value (state name)
# 'OH' - 'Ohio', 'IN' - 'Indiana'
states = {
    'OH': 'Ohio',
    'IN': 'Indiana',
    'CO': 'Colorado',
    'KY': 'Kentucky'
}

days_of_week = dict(Mon='Monday', Tues='Tuesday', Wed='Wednesday',
                    Thurs='Thursday', Fri='Friday', Sat='Saturday', Sun='Sunday')

# accessing values of a dictionary:
print(f"OH is {states['OH']}")
print(f'Mon is {days_of_week.get('Mon')}')

# add values to a dictionary
states['TS'] = 'Tennessee'
print(f'states: {states}')

# remove an entry
state_removed = states.pop('TS')
print(f'{state_removed} was removed')
print(f'states: {states}')

# p. 119 iterating over a dictionary
print("====== iterating over dictionary =========")
print(f'keys: {states.keys()}')
print("-"*10)
print(f'values: {states.values()}')
print("-"*10)
print(f'items: {states.items()}')
print("-"*10)
