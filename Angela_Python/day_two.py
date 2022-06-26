# print("Hello"[1])
#
# number = int(input("enter a 2 digit number: "))
# number1 = number // 10
# number2 = number % 10
#
# print(str(number1) + " + " + str(number2) + " = " + str(number2 + number1))
# print(number1 + number2)


#
# height = float(input("Enter your height in m: "))
# weight = int(input("Enter your weight in kg: "))
#
# bmi = (weight // (height ** 2))
# print(int(bmi))


# user_age = int(input("What is your age: "))
# standard_age = 90
# remaining_weeks = (90 - user_age) * 52
# remaining_days = (90 - user_age) * 365
# remaining_months = (90 - user_age) * 12
# print(f" You have {remaining_days} days, {remaining_weeks} weeks and {remaining_months} months left.")

print("Welcome to the tip calculator.")

user_bill = float(input("What is your total bill?: "))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15?: "))
number_of_people = int(input("How many people to split the bill?: "))

tip = user_bill * (percentage_tip / 100)
bill = (user_bill + tip) / number_of_people
total_bill = round(bill,2)
print(f"Each person should pay: {total_bill}")
