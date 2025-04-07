def search(self, arr, x):
  #check element in the arr
  if x not in arr:
    return -1
  # find the index of the first occurance of the element
  for i in range(len(arr)):
    if arr[i] == x:
      return i
