lst1 = [1, 2, 3]
lst2 = [2, 3, 4]

result = [int(num) for num in lst1 if num in lst2]
print(result)