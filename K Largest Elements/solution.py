def kLargest(self, arr, k):
    arr.sort(reverse=True)  # Sort in descending order
    return arr[:k]          # Return first k elements
