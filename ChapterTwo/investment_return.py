principal = int(input('Enter the principal amount: '))
year = int(input("enter number of year: "))

increment = float(principal * (1 + 7 / 100) ** year)
amount = principal + increment
print(f'The total amount at the end of {year} is {increment:.2f}')