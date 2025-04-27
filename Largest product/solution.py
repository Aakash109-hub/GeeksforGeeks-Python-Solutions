import math

def findMaxProduct(arr, k):
    """
    Function to find maximum product of k contiguous elements in an array
    
    Args:
    arr (list): Input array of numbers
    k (int): Number of contiguous elements
    
    Returns:
    int: Maximum product of k contiguous elements
    """
    n = len(arr)
    if n == 0 or k == 0 or k > n:
        return 0
    
    res = []
    for i in range(n - k + 1):
        res.append(math.prod(arr[i:i+k]))
    return max(res) if res else 0


# Example usage
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4], 2),
        ([1, 6, 7, 8], 3),
        ([-1, -2, -3, 4], 2),
        ([], 2),
        ([1, 2], 3)
    ]
    
    for arr, k in test_cases:
        print(f"Array: {arr}, k: {k} => Max product: {findMaxProduct(arr, k)}")
