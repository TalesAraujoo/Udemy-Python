import csv


def show_menu():
    print('------ Monthly Balance ------\n')
    print('1. Income')
    print('2. Expense')
    print('3. Report')
    print('4. Exit\n')
    option = input('Choose an option: ')
    get_option(int(option))


def get_option(chosen_option):

    match chosen_option:
        case 1:
            add_income()
            show_menu()
        case 2:
            add_expense()
            show_menu()
        case 3: 
            print()
        case 4:
            print('Exiting program...')
            print('Great job, keep shit updated!\n')


def add_income():
    with open('september.csv', 'a', newline='') as month: 
        writer = csv.writer(month)
        tmp_value = input('Income value: ')
        write_row = ['Income', tmp_value]
        writer.writerow(write_row)
        month.close()
        print('\n')


def add_expense():
    with open('september.csv', 'a', newline='') as month: 
        writer = csv.writer(month)
        tmp_value = input('Expense value: ')
        write_row = ['Expense', tmp_value]
        writer.writerow(write_row)
        month.close()
        print('\n')


show_menu()
