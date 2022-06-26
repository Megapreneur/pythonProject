deposit_amount = int(input("Enter the initial deposit amount: "))

percentage_yield = float(input("Enter annual percentage yield: "))

number_of_months = int(input("Enter maturity period (number of months): "))


month = 1
while month <= number_of_months:
    deposit_amount = deposit_amount + deposit_amount * percentage_yield / 1200

    print(f"At month {month}, the CD is worth ₦{deposit_amount:.2f}")
    month = month + 1