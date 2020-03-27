
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

    table = [[0 for x in range(capacity+1)] for y in range(n)]

    for i in range(n):
        table[i][0] = 0

    for c in range(1, capacity+1):
        if weights[0] <= c:
            table[0][c] = profits[0]

    for i in range(1, n):
        for c in range(1, capacity+1):
            w = weights[i]
            p = profits[i]
            p1 = table[i-1][c]
            if w <= c:
                p2 = p + table[i-1][c-w]
            else:
                p2 = 0
            table[i][c] = max(p1, p2)

    return table[n - 1][capacity]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
