first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
last_number = int(input("Enter last number: "))

sum = int(first_number + second_number + last_number)
average = sum / 3
product = int(first_number * second_number * last_number)

largest = first_number
if second_number > largest:
    largest = second_number
if last_number > largest:
    largest = last_number

smallest = first_number
if second_number < smallest:
    smallest = second_number
if last_number < smallest:
    smallest = last_number

print(f"sum is {sum}")
print(f"the average is {average}")
print(f"The product is {product}")
print(f"The smallest is {smallest}")
print(f"The largest is {largest}")