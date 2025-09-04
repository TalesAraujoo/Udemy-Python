archive = open('people.csv')
data = archive.read()
archive.close()

for item in data.splitlines():
    print('Nome: {}, Idade: {}'.format(*item.split(',')))
