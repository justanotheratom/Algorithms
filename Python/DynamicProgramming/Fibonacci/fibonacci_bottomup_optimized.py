
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

    ii = 0
    jj = 1
    kk = -1

    for k in range(2, n+1):
        kk = ii + jj
        ii = jj
        jj = kk

    return kk

if __name__ == '__main__':
    import doctest
    doctest.testmod()
