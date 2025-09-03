product = {'name': 'Fancy pen', 'price': 14.99,
           'imported': True, 'stock': 793}

for key in product: 
    print(key)

#OR  for key in product.keys():
#        print(key)


for value in product.values():
    print(value)

for key , value in product.items():
    print(key, value)

# In python even after the loop, the variable value
# will still be available
print('\n')
print(f'{key}: {value}')