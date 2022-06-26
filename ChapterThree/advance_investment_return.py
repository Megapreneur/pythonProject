year = 1

principal = int(input("enter the principal amount: "))
print('year    '+'amount')
while year <= 30:
    amount = float(principal * (1 + 7 / 100) ** year)

    print(f'{year}      {amount:.2f}')
    year += 1
