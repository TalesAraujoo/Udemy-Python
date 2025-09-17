# generator you will have to use 'next' to print or use each 'generated obj'
generator = (i ** 2 for i in range(10) if i % 2 == 0)

for number in generator:
    print(number)