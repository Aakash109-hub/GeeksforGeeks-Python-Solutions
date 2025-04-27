# Maximum Product of K Contiguous Elements

## Problem Statement
Given an array `arr` and an integer `k`, find the maximum product of `k` contiguous elements in the array.

### Examples:
**Input:**  
arr = [1, 2, 3, 4], k = 2  
**Output:**  
12  
**Explanation:**  
The subarray [3, 4] gives the maximum product of 12.

**Input:**  
arr = [1, 6, 7, 8], k = 3  
**Output:**  
336  
**Explanation:**  
The subarray [6, 7, 8] gives the maximum product of 336.

## Solution Approach
The solution uses a sliding window technique:
1. Iterate through all possible contiguous subarrays of size `k`
2. Calculate the product of elements in each subarray
3. Track the maximum product found

### Time Complexity
O(n*k) where:
- n is the length of the array
- k is the window size

In the worst case, we calculate the product of k elements for (n-k+1) windows.

### Space Complexity
O(n-k+1) for storing all window products (can be optimized to O(1) by tracking max product directly)
