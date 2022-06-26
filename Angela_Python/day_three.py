# print("Welcome to the rollercoster")
# height = int(input("What is your height in cm? "))
#
# if height >= 120:
#     print("You can ride the rollercoster!")
# else:
#     print("Sorry, you have to grow taller before you can ride.")

# number = int(input("Enter a number you will like to check: "))
# if number % 2 == 0:
#     print(f"{number} is an even number.")
# else:
#     print(f'{number} is an odd number.')

# height = float(input("Enter your height in m: "))
# weight = float(input("Enter your weight in kg: "))
# bmi = int(weight // (height ** 2))
# if bmi < 18.5:
#     print(f" Your bmi is {bmi}, you are underweight.")
# elif 18.5 < bmi < 25:
#     print(f'Your bmi is {bmi}, you have a normal weight.')
# elif 25 < bmi < 30:
#     print(f" Your bmi is {bmi}, you are overweight.")
# elif 30 < bmi < 35:
#     print(f"Your bmi is {bmi}, you are obese.")
# else:
#     print(f" Your bmi is {bmi}, you are clinically obese.")

# year = int(input('Which year would you like to check? '))
# if year % 4 == 0 and year % 400 == 0 and year % 100 == 0:
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")


# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
#
# if size == "S":
#     bill = 15
# elif size == "M":
#     bill = 20
# else:
#     bill = 25
# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3
# else:
#     bill = bill
# if extra_cheese == "Y":
#     bill += 1
# else:
#     bill = bill
# print(f"Your final bill is: {bill}")

# print("Welcome to the love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is your name? \n")
#
# name1_as_lower_case = name1.lower()
# combined_name = name2.lower()
#
# combined_name = combined_name + name1_as_lower_case
# t = combined_name.count("t")
# r = combined_name.count("r")
# u = combined_name.count("u")
# e = combined_name.count("e")
# l = combined_name.count("l")
# o = combined_name.count("o")
# v = combined_name.count("v")
#
#
# total = t+r+u+e+l+o+v+e
# if total < 10 or total > 90:
#     print(f"Your score is {total}, you go together like coke and mentos.")
# elif 40 < total < 50:
#     print(f"Your score is {total}, you are alright together.")
# else:
#     print(f"Your score is {total}")

print("Welcome to treasure island. \nYour mission is to find the treasure")
where = input("You're to cross a road. Where do you want to go? Type 'left' or 'right' ").lower()
what_to_do = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. ").lower()
colour_of_door = input("You arrive at the island unharmed. There is a house with 3 doors. one red, one yellow and one blue. Which colour do you choose? ").lower()
if where == "left":
    if what_to_do == "wait":
        if colour_of_door == "red":
            print("You entered a room full of fire. Game over!")
        elif colour_of_door == "yellow":
            print("You found the treasure. You won!")
        else:
            print("You entered a room of beasts. Game over")
    else:
        print("Game over, you were eaten by a shark!")
else:
    print("Game over")
