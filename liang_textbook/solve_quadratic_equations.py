import math


def quadratic_equation(a, b, c):

    r1 = (-b + math.sqrt(b**2 - 4 * a * c)) / 2 * a

    r2 = (-b - math.sqrt(b**2 - 4 * a * c)) / 2 * a

    return r1, r2



solution = quadratic_equation(1,2,1)

print(f"The roots are {solution}")