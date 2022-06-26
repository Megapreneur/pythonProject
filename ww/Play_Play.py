number = int(input("Enter a number: "))

while number != 1:
    if number % 2 != 0:
        result = number * 3 + 1
        print(result)
        break

    else:
        result = number / 2
    print(result)
    break
