def print_number(max, current):
    if current >= max:
        return
    print(current)
    print_number(max, current+1)

print_number(10, 1)