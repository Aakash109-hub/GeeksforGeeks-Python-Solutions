def search(self, arr, x):
    # Check if x is not in the array
    if x not in arr:
        return -1
    
    # Iterate through the array to find the first occurrence of x
    for i in range(len(arr)):
        if arr[i] == x:
            return i
