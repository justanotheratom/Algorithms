
# https://stackoverflow.com/questions/14132789/relative-imports-for-the-billionth-time
from Common.stack import Stack

def balancedbrackets(input):
    """
    >>> balancedbrackets('')
    True
    >>> balancedbrackets('[')
    False
    >>> balancedbrackets(']')
    False
    >>> balancedbrackets('[][')
    False
    >>> balancedbrackets('[][]')
    True
    >>> balancedbrackets('[]{)')
    False
    >>> balancedbrackets('[(){}]')
    True
    >>> balancedbrackets('[()(}]')
    False
    >>> balancedbrackets('[]')
    True
    """

    if len(input) == 0:
        return True

    s = Stack()
    validPairs = [('[', ']'), ('{', '}'), ('(', ')')]

    for c in input:
        if c in ['[', '{', '(']:
            s.push(c)
        if c in [']', '}', ')']:
            if s.isempty():
                return False
            if (s.pop(), c) not in validPairs:
                return False

    return s.isempty()

if __name__ == '__main__':
    import doctest
    doctest.testmod()
