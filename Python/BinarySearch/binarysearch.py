import math

def binarysearch_iterative(items, target):

    low = 0
    high = len(items) - 1

    while low <= high:
        mid = low + (high - low) // 2  # Do it this way to prevent integer overflow!
        if target == items[mid]:
            return True
        elif target < items[mid]:
            high = mid - 1
        elif target > items[mid]:
            low = mid + 1

    return False

def binarysearch_recursive(items, target):

    def binarysearch_internal(low, high):
        if low > high:
            return False
        mid = low + (high - low) // 2  # Do it this way to prevent integer overflow!
        if target == items[mid]:
            return True
        elif target < items[mid]:
            return binarysearch_internal(low, mid - 1)
        elif target > items[mid]:
            return binarysearch_internal(mid + 1, high)

    return binarysearch_internal(0, len(items) - 1)

def find_closest_number(items, target):

    if len(items) == 0:
        return None

    low = 0
    high = len(items) - 1

    while (low + 1) < high:
        mid = low + (high - low) // 2  # Do it this way to prevent integer overflow!
        if target == items[mid]:
            return items[mid]
        elif target > items[mid]:
            low = mid
        elif target < items[mid]:
            high = mid

    low_diff = abs(target - items[low])
    high_diff = abs(target - items[high])

    if low_diff <= high_diff:
        return items[low]
    else:
        return items[high]

def find_fixed_point(items):

    if len(items) == 0:
        return None

    low = 0
    high = len(items) - 1

    while low <= high:
        mid = low + (high - low) // 2  # Do it this way to prevent integer overflow!
        if items[mid] == mid:
            return mid
        elif items[mid] > mid:
            high = mid - 1
        elif items[mid] < mid:
            low = mid + 1

    return None

def find_bitonic_peak(items):

    if len(items) < 3:
        return None

    low = 0
    high = len(items) - 1

    while low != high:
        mid = low + (high - low) // 2  # Do it this way to prevent integer overflow!
        curr = items[mid]
        next = items[mid + 1]
        if curr > next:
            high = mid
        elif curr < next:
            low = mid + 1

    return items[low]

def find_ceiling(items, target):
    '''
    Return the smallest number greater than or equal to target.
    '''
    # TODO: Practice someday
    pass

def find_next_letter(letters, target):
    """
    Find the next letter that follows target. letters array is sorted but circular,
    so if next letter is not found, return the first letter.
    """
    # TODO: Practice someday
    pass

def find_range(items, target):
    """
    Given a sorted array of numbers with duplicates, return the
    index range that matches the target.
    """
    # TODO: Practice someday
    pass

class InfiniteArray(object):

    def __init__(self, items):
        self.items = items

    def get(self, index):
        if index < len(self.items):
            return self.items[index]
        else:
            return math.inf

def search_in_infinite_array(infinite_array, target):
    """
    Given an infinite array, return the index of target element.
    Return None if target is not found.
    """
    # TODO: Practice someday
    pass
