
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

    def fibonacci_recursive(cache, n):

        if n < 2:
            return n

        if cache[n] == -1:
            cache[n] = fibonacci_recursive(cache, n-1) + fibonacci_recursive(cache, n-2)

        return cache[n]

    cache = [-1 for x in range(n+1)]

    return fibonacci_recursive(cache, n)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
