n = int(input("Enter a number: "))

a, b = 0, 1
while a < n:
    print(a, end =' ')
    a, b = b, a+b