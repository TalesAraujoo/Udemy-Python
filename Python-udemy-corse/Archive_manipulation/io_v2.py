archive = open('people.csv')
#reading directly from the archive will 'stream' the needed data, 
#which will be much more efficient memory wise
for item in archive:
    print('Nome: {}, Idade: {}'.format(*item.split(',')))

archive.close()