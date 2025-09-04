# a = '  teste abc   '
# print(a.strip())

# b = '000 test abc 0000'
# print(b.strip('0'))
# print(b.strip('0').strip())


archive = open('people.csv')

for item in archive:
    print('Nome: {}, Idade: {}'.format(*item.strip().split(',')))

archive.close()