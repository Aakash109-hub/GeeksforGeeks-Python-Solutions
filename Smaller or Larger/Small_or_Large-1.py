def getMoreAndLess(arr, target):
    """
    Counts elements ≤ and ≥ target in a sorted array.
    
    Args:
        arr (list): Sorted list of integers.
        target (int): Target value to compare against.
    
    Returns:
        tuple: (count_≤_target, count_≥_target)
    
    Examples:
        >>> getMoreAndLess([1, 2, 8, 10, 11, 12, 19], 0)
        (0, 7)
    """
    a = b = 0
    for num in arr:
        if num <= target:
            a += 1
        if num >= target:
            b += 1
    return a, b
