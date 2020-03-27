
def knapsack(capacity, weights, profits):
    '''
    >>> knapsack(5, [2,3,1,4], [4,5,3,7])
    10
    >>> knapsack(5, [2,3,1,4], [4,7,3,7])
    11
    >>> knapsack(7, [1,2,3,5], [1,6,10,16])
    22
    >>> knapsack(6, [1,2,3,5], [1,6,10,16])
    17
    '''

    if capacity == 0:
        return 0

    if len(weights) == 0:
        return 0

    w = weights[0]
    p = profits[0]

    p1 = knapsack(capacity, weights[1::], profits[1::])

    if w <= capacity:
        p2 = p + knapsack(capacity - w, weights[1::], profits[1::])
        return max(p1, p2)
    else:
        return p1

if __name__ == '__main__':
    import doctest
    doctest.testmod()
