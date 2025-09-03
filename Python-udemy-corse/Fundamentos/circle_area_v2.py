from math import pi

radius = input('Inform the radius: ')
area = pi*int(radius)**2

print(f'The area is: {area:.2f}')
print('Module name: ', __name__)
print('Package name: ', __package__)
