def convert_number_to_roman(user_input):
    thousands = ["", "M", "MM", "MMM"]
    hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    units = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

    result = thousands[user_input // 1000] + hundreds[(user_input % 1000) // 100] + tens[(user_input % 100) // 10] \
             + units[user_input % 10]

    return result


try:

    user_input = int(input("Enter a number from 1 to 3500: "))
    if user_input > 0:
        print(convert_number_to_roman(user_input))
    else:
        print("Invalid number")

except ValueError:
    print("That was not an integer")

