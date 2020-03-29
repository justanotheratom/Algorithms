
def knapsack(capacity, weights, profits):
    '''
    :return: Maximum profit
    >>> knapsack(5, [1,2,3], [15,20,50])
    80
    >>> knapsack(8, [1,3,4,5], [15,50,60,90])
    140
    >>> knapsack(6, [1,3,4,5], [15,50,60,90])
    105
    '''

    def knapsack_recursive(capacity, index):

        if capacity == 0:
            return 0

        if index == len(weights):
            return 0

        w = weights[index]
        p = profits[index]

        p1 = knapsack_recursive(capacity, index + 1)

        if w <= capacity:
            p2 = p + knapsack_recursive(capacity - w, index)
            return max(p1, p2)
        else:
            return p1

    return knapsack_recursive(capacity, 0)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
