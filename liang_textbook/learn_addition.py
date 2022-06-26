import random

number1 = random.randint(0, 100)
number2 = random.randint(0, 100)

answer = eval(input("What is " + str(number1) + " + " + str(number2) + "? "))

print(number1, " + ", number2, "=", answer, "is", number1 + number2 == answer)