def non_duplicate_value(lst):
    for i in range(0, len(lst) - 1, 2):
        if lst[i] != lst[i + 1]:
            return lst[i]

    if lst[-1] != lst[-2]:
        return lst[-1]
    return -1


x = [1, 1, 2, 2, 3, 3]

print(non_duplicate_value(x))
