# Exiting with error without running the rest of the code
from math import pi
import sys
import errno


ERRO = '\033[91m'
NORMAL = '\033[0m'


def circle(radius):
    area = pi * float(radius) ** 2
    return area


def help():
    print("It is mandatory to inform the circle's radius.")
    print(f'Syntax: {sys.argv[0]} <radius>')
    

if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(1)
        sys.exit(errno.EPERM)
    
    if not sys.argv[1].isnumeric():
        help()
        print(ERRO + 'The radius must be a numeric value' + NORMAL)
        sys.exit(errno.EINVAL)
    
    radius = sys.argv[1]
    area = circle(radius)
    print(f"Circle's area: {area:.2f}")
    