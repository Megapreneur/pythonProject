import math


def area_of_pentagon(s):

    area = (5 * s**2)/ (4 * math.tan(math.pi/5))
    return area


pentagon = area_of_pentagon(5.5)
print(pentagon)
