user_input = int(input("Enter a number to check: "))

count = 1


while count <= (user_input // 2):
    if user_input % count == 0:

        print(count, "is a factor of", user_input)
    count += 1





