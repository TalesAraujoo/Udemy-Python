# 0, 1, 1, 2, 3, 5, 8, 13, 21...

def fibonacci(limit):
    result = [0, 1]
    
    while result[-1] < limit:
        # -1 last item, -2 second to last
        result.append(result[-1] + result[-2])
    return result
      

if __name__ == '__main__':
    # for in the fibonacci list (return result)
    for number in fibonacci(10000):
        print(number)