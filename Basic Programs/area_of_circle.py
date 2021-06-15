# formula
# area = PI * R*R
from math import pi


def area(R):
    return (R * R) * pi


print(area(int(input("Enter Radius: "))))
