from math import pi
import sys

def circle(radius):
    area = pi * float(radius) ** 2
    return area

if __name__ == '__main__':
   #  print(sys.argv[0]) # returns the file name
   #  print(sys.argv[1]) # returns the first sys argument
    radius = sys.argv[1]
    area = circle(radius)
    print(f"Circle's area: {area:.2f}")