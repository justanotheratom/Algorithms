
def partitionswithequalsubsetsum(nums):
    '''
    :param nums: list of numbers
    :return: Whether or not the list can be partitioned into subsets with equal sum
    >>> partitionswithequalsubsetsum([1,2,3,4])
    True
    >>> partitionswithequalsubsetsum([1,1,3,4,7])
    True
    >>> partitionswithequalsubsetsum([2,3,4,6])
    False
    '''

    elements = len(nums)

    if elements < 2:
        return False

    total = sum(nums)

    if total % 2 != 0:
        return False

    targetsum = total // 2

    table = [[False for x in range(targetsum+1)] for y in range(elements)]

    for i in range(elements):
        table[i][0] = True

    for t in range(1, targetsum+1):
        table[0][t] = (nums[0] == t)

    for i in range(1, elements):
        for t in range(1, targetsum+1):
            n = nums[i]
            if (table[i-1][t]):
                table[i][t] = True
            elif n <= t:
                table[i][t] = table[i-1][t-n]

    return table[elements-1][targetsum] == 1

if __name__ == '__main__':
    import doctest
    doctest.testmod()
