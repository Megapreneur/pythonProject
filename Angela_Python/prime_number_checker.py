def prime_checker(number):
    for i in range(2, number):
        if number % i == 0:
            return "it is not a prime number"
        else:
            return "it's a prime number"


n = int(input("Check this number: "))
print(prime_checker(number=n))

