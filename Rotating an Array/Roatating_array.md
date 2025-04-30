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


### The idea behind the reversal algorithm:
The reversal algorithm is a clever way to rotate an array without needing extra space. Instead of shifting elements one by one, we **reverse parts of the array** in a way that achieves rotation efficiently. Here’s how it works:

### Steps in the function:
1️⃣ **Handle cases where d > n**  
   - `d %= n` ensures that if `d` is greater than `n`, we only rotate the remainder (`d % n`).  
   - Example: If `n = 5` and `d = 7`, rotating by `7` is the same as rotating by `7 % 5 = 2`.

2️⃣ **Reverse the entire array**  
   - `arr.reverse()` flips the array completely.  
   - Example: If `arr = [1, 2, 3, 4, 5]`, after reversing it becomes `[5, 4, 3, 2, 1]`.

3️⃣ **Reverse the first (n-d) elements**  
   - `arr[:n-d] = reversed(arr[:n-d])` reverses the first section of the array.  
   - Example: If `n = 5` and `d = 3`, we reverse the first `5-3 = 2` elements.  
   - `arr[:2]` → `[5, 4]` → reversed → `[4, 5]`  
   - New array: `[4, 5, 3, 2, 1]`

4️⃣ **Reverse the last d elements**  
   - `arr[n-d:] = reversed(arr[n-d:])` reverses the remaining section.  
   - Example: `arr[2:]` → `[3, 2, 1]` → reversed → `[1, 2, 3]`  
   - Final array: `[4, 5, 1, 2, 3]` → 🎯 Expected Output!

### Why does this work?
By reversing different sections of the array **in a strategic way**, we simulate a rotation without shifting elements individually. This results in a **time-efficient and space-efficient** solution.
