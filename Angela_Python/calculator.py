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


def calculator():
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the second number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input("Type 'y' to continue calculating or 'n' to end calculating: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()

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
