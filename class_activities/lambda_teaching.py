# add = lambda x, y: x + y
# sub = lambda x, y: x - y
# print(add.__name__)
# print(sub.__name__)
def add(a, b):
    return a + b


def sub(c, d):
    return d - c


def multiply(g, f):
    return g * f


def operate(x, y, fn):
    return fn(x, y)


def calculate(x, y, z):
    return x + y - z


def operation(x, y, z, fn):
    return fn(x, y, z)


val_calculate = operation(4, 2, 6, calculate)
val_sub = operate(5, 24, sub)
val_add = operate(5, 24, add)
val_multiply = operate(5, 4, multiply)
div = operate(5, 24, lambda x, y: y / x)
val_sub2 = operate(4, 60, lambda x, y: y - x)
val_add2 = operate(6, 4, lambda x, y: x + y)
val_calculate2 = operation(4, 5, 6, lambda x, y, z: x + y - z)


def multiple(x, fun):
    return fun(x)


val_double = multiple(3, lambda x: x ** 2)
val_triple = multiple(3, lambda x: x ** 3)

print(val_add)
print(val_sub)
print(val_multiply)
print(val_calculate)
print(div)
print(val_sub2)
print(val_add2)
print(val_calculate2)
print(val_double)
print(val_triple)


print(any([True, False, True]))

names = ["Amaka", "Segun", "comb", "Samson", "foil"]

print(all([name.istitle() for name in names]))

print(all([name.istitle() for name in names]))


peoples = [
    {"name": "Omosetan Omorele", "age": 30, "year_of_exp": 4, "language": ["Python", "Java"]},
    {"name": "John Doe", "age": 25, "year_of_exp": 2, "language": ["Python", "JavaScript"]},
    {"name": "Amaka Philip", "age": 19, "year_of_exp": 5, "language": ["C#", "Java"]},
    {"name": "Florence Segun", "age": 28, "year_of_exp": 15, "language": ["Python"]},
    {"name": "Ademola Megbabi", "age": 20, "year_of_exp": 10, "language": ["Python", "Java", "C#", "C+"]},
    {"name": "Ayoola Megbabi", "age": 10, "year_of_exp": 3, "language": ["Python", "Java", "C#", "C+"]}
]

# print([True if people["age"] <= 20 else False for people in peoples])
print([people["age"] <= 20 and "Python" in people["language"]for people in peoples])
print(all(people["age"] <= 20 and "Python" in people["language"]for people in peoples))
print(any(people["age"] <= 20 and "Python" in people["language"]for people in peoples))
print([people["age"] <= 20 for people in peoples])
print([people["name"] for people in peoples if people["age"] <= 20 and "Python" in people["language"]])
