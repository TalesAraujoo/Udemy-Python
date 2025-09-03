from math import pi


def circle_area(radius):
   area = pi*int(radius)**2
   print(f'The area is: {area:.2f}') 


if __name__ == '__main__':
    radius = input('Inform the radius: ')
    circle_area(radius)  