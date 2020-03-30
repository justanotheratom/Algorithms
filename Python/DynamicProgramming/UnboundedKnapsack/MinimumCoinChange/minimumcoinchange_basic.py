import math

def minimumcoinchange(target, denominations):
    '''
    :return: Minimum number of coins needed to make the change
    >>> minimumcoinchange(5, [1,2,3])
    2
    >>> minimumcoinchange(11, [1,2,3])
    4
    '''

    def minimumcoinchange_recursive(target, index):

        if target == 0:
            return 0

        if index == len(denominations):
            return math.inf                # !!! This is important!

        v = denominations[index]

        c1 = minimumcoinchange_recursive(target, index + 1)

        if v <= target:
            c2 = 1 + minimumcoinchange_recursive(target - v, index)
            return min(c1, c2)
        else:
            return c1

    return minimumcoinchange_recursive(target, 0)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
