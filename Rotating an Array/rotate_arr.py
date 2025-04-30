def leftRotate(arr, d):
    n = len(arr)

    d %= n  # Handle cases where d > n

    arr.reverse()  # Reverse the entire array
    arr[:n-d] = reversed(arr[:n-d])  # Reverse the first (n-d) elements
    arr[n-d:] = reversed(arr[n-d:])  # Reverse the last d elements

    return arr
