user_input = int(input("Enter a number to check: "))

count = 1
sum_of_factors = 0

while count <= (user_input // 2):
    if user_input % count == 0:
        sum_of_factors += count
        print(count, "is a factor of", user_input)
    count += 1
print(sum_of_factors)

if sum_of_factors == user_input:
    print(user_input, "is a perfect number")
elif sum_of_factors > user_input:
    print(user_input, "is an abundant number")
else:
    print(user_input, "is a deficient number")
