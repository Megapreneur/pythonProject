user_input = int(input("Enter a number: "))
product = 1
for i in range(1, user_input + 1):
    product *= i
print(product)


# total = 0
# for i in range(1, user_input+1):
#     total += i
#     print(total)
#
# smiley = "\U0001f600"
# for i in range(1, 21, 2):
#     print(f"{smiley * i :^20}")
#
#
#
# smiley = "\U0001f601"
# for i in range(1, 11):
#     print(f"{smiley * i :<10}   {smiley * (11- i) :<10} {smiley * (11- i) :>20} {smiley * i :>10} ")
#
#
#
# for index, letter in enumerate("Hello world"):
#     print(f"{letter} is in index {index}")

