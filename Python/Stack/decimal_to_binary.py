
# https://stackoverflow.com/questions/14132789/relative-imports-for-the-billionth-time
from Common.stack import Stack

def decimal_to_binary(decimal):
    """
    Convert a decimal int to a string in binary format
    >>> decimal_to_binary(0)
    '0'
    >>> decimal_to_binary(1)
    '1'
    >>> decimal_to_binary(2)
    '10'
    >>> decimal_to_binary(3)
    '11'
    >>> decimal_to_binary(4)
    '100'
    >>> decimal_to_binary(10)
    '1010'
    """

    if decimal == 0:
        return '0'

    s = Stack()

    while decimal != 0:
        quotient  = decimal // 2
        remainder = decimal % 2
        s.push(str(remainder))
        decimal = quotient

    result = ''
    while not s.isempty():
        result += s.pop()

    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()
