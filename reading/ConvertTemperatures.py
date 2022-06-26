def convert_celsius_to_fahrenheit(c):
    answer = c * (9 / 5) + 32
    return answer


def convert_fahrenheit_to_celsius(f):
    result = (f - 32) * (5 / 9)
    return result


a = float(input("Enter a temperature in degrees F: "))
temp = convert_fahrenheit_to_celsius(a)
print(f"{temp:.2f}")

b = float(input("Enter a temperature in degrees C: "))
temp2 = convert_celsius_to_fahrenheit(b)
print(f"{temp2:.2f}")