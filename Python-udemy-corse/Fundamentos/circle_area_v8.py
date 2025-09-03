# function help implemented to shorten the code
from math import pi
import sys

def circle(radius):
    area = pi * float(radius) ** 2
    return area


def help():
    print(f""""\
            It is mandatory to inform the circle's radius.
            Syntax: {sys.argv[0]} <radius>""")
    

if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
    else: 
        radius = sys.argv[1]
        area = circle(radius)
        print(f"Circle's area: {area:.2f}")
