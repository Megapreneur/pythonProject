num = 1
while num <= 100:
    if num % 3 == 0 and num % 5 == 0:
        print("FIZZBUZZ")
    elif num % 5 == 0:
        print("BUZZ")
    elif num % 3 == 0:
        print("FIZZ")
    else:
        print(num)
    num +=1
