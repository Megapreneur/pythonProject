lst = list(map(lambda x: x ** 2, range(1, 10)))

print(lst)

map_object = map(lambda x: x ** 2, range(1, 10))
lst1 = list(map_object)
lst2 = list(map_object)
print("1", lst1)
print("2", lst2)

map_object1 = map(lambda x: x ** 2 if x % 2 == 0 else x, range(1, 10))
lst1 = list(map_object1)
lst2 = list(map_object1)
print("1", lst1)
print("2", lst2)


def isEven(x):
    return x % 2 == 0


filter_obj = list(filter(isEven, range(1, 10)))
print(filter_obj)



from functools import reduce
fruits = ["Apple", "Pear", "Pineapples", "Orange", "Watermelon", "Banana", "Cucumber"]
longest = reduce(lambda x, y: x if len(x) > len(y)  else y, fruits)
print(longest)

smallest = reduce(lambda x, y: x if len(x) < len(y)  else y, fruits)
print(smallest)

print(max(fruits, key=len))
print(min(fruits, key=len))
print(sorted(fruits, key=len))
print(sorted(fruits, key=len, reverse=True))
print(sorted(fruits, key=lambda x: x[-1]))

