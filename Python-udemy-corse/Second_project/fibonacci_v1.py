# 0, 1, 1, 2, 3, 5, 8, 13, 21...

def fibonacci():
    #last but one
    # penultimate    
    second_to_last = 0
    last = 1
    print(f'{second_to_last}, {last}', end =',')

    while True:
        next = last + second_to_last
        print(next, end = ',')
        second_to_last = last
        last = next

if __name__ == '__main__':

    fibonacci()