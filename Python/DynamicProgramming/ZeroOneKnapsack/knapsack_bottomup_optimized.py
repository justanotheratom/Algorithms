
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

    n = len(profits)

    table = [0 for x in range(capacity+1)]

    for c in range(capacity+1):
        if weights[0] <= c:
            table[c] = profits[0]

    for i in range(1, n):
        for c in range(capacity, 0, -1):
            w = weights[i]
            p = profits[i]
            p1 = table[c]
            if w <= c:
                p2 = p + table[c-w]
            else:
                p2 = 0
            table[c] = max(p1, p2)

    return table[capacity]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
