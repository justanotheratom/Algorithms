
def countways(n):
    '''
    Given a staircase with n steps, find the number of was you can climb it
    by taking 1 step, 2 steps, or 3 steps at each turn.
    :param n: Number of steps in the staircase
    :return: Number of possible ways.
    >>> countways(0)
    1
    >>> countways(1)
    1
    >>> countways(2)
    2
    >>> countways(3)
    4
    >>> countways(4)
    7
    >>> countways(5)
    13
    >>> countways(6)
    24
    '''

    # TODO : Implement bottom-up table based solution

if __name__ == '__main__':
    import doctest
    doctest.testmod()
