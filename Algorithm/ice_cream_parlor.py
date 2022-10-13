m = 9

arr = [1,2,3,4,6,8,9,5]
lst = []
for i in arr:
    for j in arr:
        if i + j == m:
            lst.append(i)
            lst.append(j)
    break

print(lst)