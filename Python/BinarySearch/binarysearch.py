
def binarysearch_iterative(items, target):

    low = 0
    high = len(items) - 1

    while low <= high:
        mid = (low + high) // 2
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
        mid = (low + high) // 2
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
        mid = (low + high) // 2
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
        mid = (low + high) // 2
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
        mid = (low + high) // 2
        prev = items[mid - 1]
        curr = items[mid]
        next = items[mid + 1]
        if prev < curr > next:
            return curr
        elif prev > curr > next:
            high = mid - 1
        elif prev < curr < next:
            low = mid + 1
        else:
            return None

    return None
