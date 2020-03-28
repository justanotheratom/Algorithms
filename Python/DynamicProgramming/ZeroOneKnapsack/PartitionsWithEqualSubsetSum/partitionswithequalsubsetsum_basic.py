
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

    def hassubsetwithtargetsum(target, index):

        if target == 0:
            return True

        if index == len(nums):
            return False

        n = nums[index]

        if n <= target:
            if hassubsetwithtargetsum(target - n, index + 1):
                return True

        return hassubsetwithtargetsum(target, index + 1)

    total = sum(nums)

    if total % 2 != 0:
        return False

    target = total / 2

    return hassubsetwithtargetsum(target, 0)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
