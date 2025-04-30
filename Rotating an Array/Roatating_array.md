# Array Rotation using Reversal Algorithm  

## Problem Statement  
Given an array `arr[]`, the task is to rotate the array by `d` elements where `d ≤ arr.size`.  

### Example  

#### Input:  
```plaintext
arr[] = [-1, -2, -3, 4, 5, 6, 7]
d = 2
```

#### Output:  
```plaintext
[-3, 4, 5, 6, 7, -1, -2]
```

### Explanation:  
- **Rotate by 1:** `[-2, -3, 4, 5, 6, 7, -1]`
- **Rotate by 2:** `[-3, 4, 5, 6, 7, -1, -2]`

## Solution Approach  
This solution implements **the reversal algorithm** to rotate the array efficiently without using extra space. The steps involved are:  
1. **Reverse the entire array.**  
2. **Reverse the first (n-d) elements.**  
3. **Reverse the last d elements.**  


