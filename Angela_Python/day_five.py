# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " pie")
# print(fruits)

# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# print(student_heights)
# total_height = sum(student_heights)

# total_height = 0
# number_of_students = 0
# for height in student_heights:
#     total_height += height
#     number_of_students += 1
#
#
# average_height = round(total_height / number_of_students)
# print(average_height)

#
# largest_number = 0
# for number in student_heights:
#     if number > largest_number:
#         largest_number = number
# print(f"The highest score int the class is: {largest_number}")

# sum = 0
# for number in range(2, 101, 2):
#     sum += number
# print(sum)

# for number in range(1, 101):
#     if number % 15 == 0:
#         print("FizzBuzz")
#     elif number % 5 == 0:
#         print("Buzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     else:
#         print(number)
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K' 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '₦', '%', '&', '(', ')', '*', '+']
password = []
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

for i in range(nr_letters):
    password.append(random.choice(letters))
for i in range(nr_symbols):
    password.append(random.choice(symbols))
for i in range(nr_numbers):
    password.append(random.choice(numbers))
random.shuffle(password)
for i in password:
    print(i, end="")