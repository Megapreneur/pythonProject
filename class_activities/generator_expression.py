import sys

gen = (num for num in range(1, 11*100))

print(sys.getsizeof((gen)))
# print(sys.getsiozeof(lst))


dict_comp = {k: v for k, v in zip(range(5), range(5))}
print(dict_comp)