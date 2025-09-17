with open('people.csv') as archive:
    for register in archive:
        print('Name: {} Age: {}'.format(*register.strip().split(',')))

# com with, o próprio python faz o gerenciamento de memória e fecha o 
# arquivo que foi aberto temporariamente