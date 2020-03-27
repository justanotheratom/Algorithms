
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

    def knapsack_recursive(capacity, index):

        if capacity == 0:
            return 0

        if index == len(weights):
            return 0

        if cache[index][capacity] != -1:
            return cache[index][capacity]

        w = weights[index]
        p = profits[index]

        p1 = knapsack_recursive(capacity, index + 1)

        if w <= capacity:
            p2 = p + knapsack_recursive(capacity - w, index + 1)
            return max(p1, p2)
        else:
            return p1

    cache = [[-1 for x in range(capacity+1)] for y in range(len(profits))]

    return knapsack_recursive(capacity, 0)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
