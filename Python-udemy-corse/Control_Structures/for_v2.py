phrase = 'paralelepipedo'

count_a = 0
count = 0
for char in phrase:
    count += 1
    print(f'{char}', end= ' ')

    if char == 'a':
        count_a += 1

print('\n')
print(f'Number of letters = {count}')
print(f'Number of letters A: {count_a}')

print('\n')

# ------ Lists -----
passed = ['Rafaela', 'Pedro', 'Renato', 'Tales']

for name in passed:
    print(name, end = ' ')

print('\n') 

# ----- enumerated Lists ------
for position, name in enumerate(passed):
    print(position + 1, name)


# ----- TUPLES -----
week_days = ('Sunday','Monday', 'Tuesday', 'Wednesday',
             'Thursday', 'Friday', 'Saturday')

for day in week_days:
    print(day)

# ----- SETS -------
for letter in set('muito legal'):
    print(letter)

for letter in {1, 2, 3, 4, 5, 6}:
    print(letter)