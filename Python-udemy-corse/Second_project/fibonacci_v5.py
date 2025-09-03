# 0, 1, 1, 2, 3, 5, 8, 13, 21...

def fibonacci(limit):
    result = [0, 1]
    
    while result[-1] < limit:
        #  -2: from second to last until last (:)
        result.append(sum(result[-2:]))
    return result
      

if __name__ == '__main__':
    # for in the fibonacci list (return result)
    for number in fibonacci(10000):
        print(number)

        