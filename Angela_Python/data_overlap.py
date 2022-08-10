lst1 = [1, 2, 3, 23, 4, 11, 7]
lst2 = [2, 3, 4, 11, 8, 21]

result = [int(num) for num in lst1 if num in lst2]
print(result)