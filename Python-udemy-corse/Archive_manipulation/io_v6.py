with open('people.csv') as archive:
    with open('people.txt', 'w') as exit:
        for register in archive:
            person = register.strip().split(',')
            print('Name: {} Age: {}'.format(*person), file=exit)

if archive.closed:
    print('The archive has been closed')   

if exit.closed:
    print('The exit file is also closed!')         