import bisect

def getMoreAndLess(arr, target):
    """
    Optimized version using binary search (requires sorted array).
    
    Examples:
        >>> getMoreAndLess([1, 5, 8, 12, 12, 12, 19], 12)
        (6, 4)
    """
    left = bisect.bisect_right(arr, target)  # Elements ≤ target
    right = len(arr) - bisect.bisect_left(arr, target)  # Elements ≥ target
    return left, right
