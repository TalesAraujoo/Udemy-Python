# 0, 1, 1, 2, 3, 5, 8, 13, 21...

def fibonacci(qty):
    result = [0, 1]
    
    while True:
        result.append(sum(result[-2:]))
        if len(result) == qty:
            break
        return result
      

if __name__ == '__main__':
    # for in the fibonacci list (return result)
    for number in fibonacci(30):
        print(number)

        