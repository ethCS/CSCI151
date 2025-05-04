#Tell me what this function does?

number = 10

def mystery_converter(number):
    if number == 0:
        return "0"

    result = ""

    while number > 0:
        remainder = number % 2
        result = str(remainder) + result
        number = number // 2

    return result

#2 = 10
#3 = 11
#4 = 100
#5 = 1010
