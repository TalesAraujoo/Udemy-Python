dictionary = {i: i * 2 for i in range(10) if i % 2 == 0}

print(dictionary)

for numero, dobro in dictionary.items():
    print(f'{numero} x 2: {dobro}')