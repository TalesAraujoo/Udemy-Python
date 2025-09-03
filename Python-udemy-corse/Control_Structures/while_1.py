#while True:
#   print("It's gonna take forever!\n")

from random import randint

user_number = -1
secret_number = randint(1, 10)

while user_number != secret_number:
    user_number = int(input('Type a number: '))

    if user_number == secret_number:
        print('You got it!!!')
    else:
        print('You failed! Try again!\n')