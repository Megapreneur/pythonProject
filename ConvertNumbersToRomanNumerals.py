
def convertNumberToRoman(number):

    thousands = ["", "M", "MM", "MMM"]
    hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    units = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

    result = thousands[number // 1000] + hundreds[(number % 1000) // 100] + tens[(number % 100) // 10] + units[number % 10]

    return result


print(convertNumberToRoman(2022))




