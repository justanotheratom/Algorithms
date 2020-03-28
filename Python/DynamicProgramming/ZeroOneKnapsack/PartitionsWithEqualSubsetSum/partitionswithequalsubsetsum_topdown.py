
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

    def hassubsetwithtargetsum(index, target):

        if target == 0:
            return 1

        if index == len(nums):
            return 0

        if cache[index][target] != -1:
            return cache[index][target]

        n = nums[index]

        result =  hassubsetwithtargetsum(index + 1, target)

        if n <= target:
            result |= hassubsetwithtargetsum(index + 1, target - n)

        cache[index][target] = result

        return result

    total = sum(nums)

    if total % 2 != 0:
        return False

    target = total // 2

    cache = [[-1 for x in range(target+1)] for y in range(len(nums))]

    return hassubsetwithtargetsum(0, target) == 1

if __name__ == '__main__':
    import doctest
    doctest.testmod()
