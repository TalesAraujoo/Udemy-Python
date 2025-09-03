# for i in range(1, 11):
#     if i == 6:
#         break
#     print(i)

# print('The end!')


#function dice_raffle numbers between 1 and 6
# for with range 1 to 6
# if number is odd, continue
# if number is even and equal to the raffled number
# from the function, print 'YOU GOT IT!' and break it
# if you don't get it, print 'NOT THIS TIME BUD!

from random import randint

def dice_raffle(number):
    rand_number = randint(1, 6)
    print(f'The dice number is {rand_number}')

    if number % 2 == 0 and number == rand_number:
        print('YOU GOT IT!!!')
    else:
        print('NOT THIS TIME BUD!!! =(')   


while True:
    number = input('Pick a number from 1 to 6: ')

    if number.isnumeric():
        number = int(number)
    else:
        print('Type ONLY numbers and from 1 to 6\n')
        continue
    
           
    # print(f'Module?? {number % 2}')
    if 1 <= number <= 6:
        dice_raffle(number)
        print('\n')

        continue_game = input('Do you wanna play again? (y/n): ')
    
        if continue_game.lower() == 'y':
            continue
        elif continue_game.lower() =='n':
            print('BYE!!!\n')
            break
        else:
            print('Type Y or N\n')
            
    else:
        print('IT MUST BE FROM 1 to 6!!!!\n')
