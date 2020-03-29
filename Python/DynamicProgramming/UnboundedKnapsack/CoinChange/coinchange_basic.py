
def coinchange(target, denominations):
    '''
    :return: Total number of distinct ways to make the target amount
    >>> coinchange(5, [1,2,3])
    5
    '''

    def coinchange_recursive(target, index):

        if target == 0:
            return 1

        if index == len(denominations):
            return 0

        v = denominations[index]

        c1 = coinchange_recursive(target, index + 1)

        if v <= target:
            c2 = coinchange_recursive(target - v, index)
            return c1 + c2
        else:
            return c1

    return coinchange_recursive(target, 0)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
