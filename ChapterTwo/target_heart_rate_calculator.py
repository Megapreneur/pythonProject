user_age = int(input('What is your age? '))

maximum_heart_rate = 220 - user_age

target_heart_rate = (50/100) * maximum_heart_rate
target_heart_rate2 = (85/100) * maximum_heart_rate

print(f"Your maximum heart rate is {maximum_heart_rate} and your target heart rate is {target_heart_rate} - {target_heart_rate2}.")