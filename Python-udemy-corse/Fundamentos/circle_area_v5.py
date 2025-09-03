from math import pi


def circle_area(radius):
   area = pi*int(radius)**2
   return area


if __name__ == '__main__':
    radius = input('Inform the radius: ')
    area = circle_area(radius)  
    print(f"The circle's area is: {area:.2f}")