# validacao do argv
from math import pi
import sys

def circle(radius):
    area = pi * float(radius) ** 2
    return area

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f""""\
            It is mandatory to inform the circle's radius.
            Syntax: {sys.argv[0]} <radius>""")
    else: 
        radius = sys.argv[1]
        area = circle(radius)
        print(f"Circle's area: {area:.2f}")