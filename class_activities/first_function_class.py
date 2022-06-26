# def get_digit(number, position):
#     '''return digit at position in number, counting from right'''
#     # assert 4 == 2, "4 is not equal 2"
#     return number // (10 ** position) % 10
#
# print(get_digit(23457, 1))

def get_number(number: int, position: int) -> int:
    """
    Get the digit at a particular position
    >>> get_number(234,0)
    4
    >>> get_number(234, 2)
    2
    >>> get_number(237456, 3)
    7
    >>> "hello"
    'hello'

    """
    return number // (10 ** position) % 10

