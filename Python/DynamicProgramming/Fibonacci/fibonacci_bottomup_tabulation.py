
def fibonacci(n):
    """
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    1
    >>> fibonacci(3)
    2
    >>> fibonacci(30)
    832040
    """
    if n < 2:
        return n

    table = [0 for x in range(n+1)]
    table[0] = 0
    table[1] = 1

    for i in range(2, n+1):
        table[i] = table[i-1] + table[i-2]

    return table[n]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
