def sum_2(a, b):
    return a + b

def sum_3(a, b, c):
    return a + b + c

def sum_n(*numeros):
    soma = 0
    for n in numeros:
        soma += n
    return soma
    
#packing 
print(sum_2(1, 2))
print(sum_n(1, 2, 3, 4))

#unpacking
tuple_nums = (1, 2, 3)
# it will unpack these 3 items inside nums and estabilish them as arguments
print(sum_3(*tuple_nums))

list_nums = [2, 3, 6]
print(sum_3(*list_nums))