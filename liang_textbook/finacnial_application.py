year = 0

principal_amount = 10000

while year < 10:
    principal_amount = principal_amount + (principal_amount * 5 / 100)
    year = year + 1

print(f'The amount of {year} is {principal_amount:.2f}')


future_year = 0
while future_year < 4:
    principal_amount = principal_amount + (principal_amount * 5 / 100)
    future_year = future_year + 1

print(f'The amount of {year + future_year} is {principal_amount:.2f}')
