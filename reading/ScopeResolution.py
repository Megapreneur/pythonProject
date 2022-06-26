# x = 5
#
#
# def outer_func():
#     y = 3
#
#     def inner_func():
#         z = x + y
#         return z
#
#     return inner_func()

total = 1


def add_to_total(n):
    global total
    total = total + n


add_to_total(5)
print(total)
