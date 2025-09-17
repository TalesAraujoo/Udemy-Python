try: 
    archive = open('people.csv')

    for item in archive:
        print('Nome: {}, Idade: {}'.format(*item.strip().split(',')))
finally:
    print('finally')
    archive.close()

if archive.closed:
    print('The archive has been closed!')