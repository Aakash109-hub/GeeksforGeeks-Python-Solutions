def findExtra(self, arr1, arr2):
    n = len(arr2)
    
    for i in range(n):
        if arr1[i] != arr2[i]:
            return i
    return n
