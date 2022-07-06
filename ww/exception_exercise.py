def user():
    try:
        user_input = int(input("Enter a number: "))
        print(f"The number you entered is {user_input}")
    except ValueError:
        print("Wrong input. Try again")
        user()


user()


