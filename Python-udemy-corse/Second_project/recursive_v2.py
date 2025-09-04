# 0, 1, 1, 2, 3, 5, 8, 13, 21...

def fibonacci_recursive(qty, sequence=(0, 1)):
    if len(sequence) == qty:
        return sequence
    return fibonacci_recursive(qty, sequence + (sum(sequence[-2:]),))         


if __name__ == '__main__':
    # for in the fibonacci list (return result)
    for number in fibonacci_recursive(20):
        print(number)

        