# (Find the number of days in a month) Write a program that prompts the user to
# enter the month and year and displays the number of days in the month. For exam-
# ple, if the user entered month 2 and year 2000 , the program should display that
# February 2000 has 29 days. If the user entered month 3 and year 2005 , the pro-
# gram should display that March 2005 has 31 days


user_input = int(input("Enter an integer between 1 to 12: "))
user_input_year = int(input("Enter a year: "))


if user_input == 1:
    month = "January"
    days = 31
elif user_input == 2:
    month = "February"
    if user_input_year % 4 == 0 and user_input_year % 100 != 0 or user_input_year % 400 == 0:
        days = 29
    else:
        days = 28
elif user_input == 3:
    month = "March"
    days = 31
elif user_input == 4:
    month = "April"
    days = 30
elif user_input == 5:
    month = "May"
    days = 31
elif user_input == 6:
    month = "June"
    days = 30
elif user_input == 7:
    month = "July"
    days = 31
elif user_input == 8:
    month = "August"
    days = 31
elif user_input == 9:
    month = "September"
    days = 30
elif user_input == 10:
    month = "October"
    days = 31
elif user_input == 11:
    month = "November"
    days = 30
else:
    month = "December"
    days = 31

print(f"{month} {user_input_year} has {days} days")