
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

    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
