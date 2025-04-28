def count_digit_occurrence(k, arr):
    """
    Counts total occurrences of digit `k` in all numbers of array `arr`.

    Args:
        k (int): Digit to count (0-9).
        arr (list): List of integers.

    Returns:
        int: Total count of digit `k`.

    Examples:
        >>> count_digit_occurrence(1, [11, 12, 13, 14, 15])
        6
    """
    k_str = str(k)
    total = 0
    for num in arr:
        total += str(num).count(k_str)
    return total
