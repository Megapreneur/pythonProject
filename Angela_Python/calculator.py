# Calculator


# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

num1 = int(input("What's the first number?: "))
for key in operations:
    print(key)
operation_symbol = input("Pick an operation from the line above: ")
num2 = int(input("What's the second number?: "))
calculation_function = operations[operation_symbol]
first_answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {first_answer}")
should_continue = input("Type 'y' to continue calculating or 'n' to end calculating: ")

while

operation_symbol = input("Pick another operation: ")
num3 = int(input("What's the second number?: "))
calculation_function = operations[operation_symbol]
second_answer = calculation_function(first_answer, num3)

print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")


# if operation_symbol == "+":
#     answer = add(num1, num2)
# elif operation_symbol == "-":
#     answer = subtract(num1, num2)
# elif operation_symbol == "*":
#     answer = multiply(num1, num2)
# elif operation_symbol == "/":
#     answer = divide(num1, num2)
# else:
#     print("Invalid sign")

