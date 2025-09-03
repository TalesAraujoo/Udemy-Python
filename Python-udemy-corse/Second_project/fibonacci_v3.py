# 0, 1, 1, 2, 3, 5, 8, 13, 21...

def fibonacci(limit):
    #last but one
    # penultimate    
    second_to_last = 0
    last = 1
    print(f'{second_to_last}, {last}', end =',')

    while last < limit:
        #changed the structure with the packing method
        # where we dont need a 3rd variable to swap values between variables
        # e.g: a, b = b, a 
        second_to_last, last = last, last + second_to_last
        print(last, end = ', ')

if __name__ == '__main__':

    fibonacci(10000)