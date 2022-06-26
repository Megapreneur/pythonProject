user_response = int(input("Enter today's day: "))
user_response2 = int(input("Enter the number of days elapsed since today:  "))


if user_response == 0:
    today = "sunday"
elif user_response == 1:
    today = "monday"
elif user_response == 2:
    today = "tuesday"
elif user_response == 3:
    today = "wednesday"
elif user_response == 4:
    today = "thursday"
elif user_response == 5:
    today = "friday"
else:
    today = "saturday"

if user_response2 % 7 == 0:
    future_day = "sunday"
elif user_response2 % 7 == 1:
    future_day = "monday"
elif user_response2 % 7 == 2:
    future_day = "tuesday"
elif user_response2 % 7 == 3:
    future_day = "wednesday"
elif user_response2 % 7 == 4:
    future_day = "thursday"
elif user_response2 % 7 == 5:
    future_day = "friday"
else:
    future_day = "saturday"
print(f"Today is {today} and the future day is {future_day}")