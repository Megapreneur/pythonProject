def prime_checker(number):
    half_number = number // 2
    for i in range(2, half_number):
        if half_number % i == 0:
            return "it's a prime number"
        else:
            return "it is not a prime number"


n = int(input("Check this number: "))
print(prime_checker(number=n))

