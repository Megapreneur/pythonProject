import random

random = random.randint(0, 100)
print("Guess a magic number between 0 and 100")
user_input = -1
while user_input != random:
    user_input = int(input("Guess the number: "))
    if user_input == random:
        print("You are correct")
    elif user_input < random:
        print("Your number is too low")
    else:
        print("Your number is too high")
