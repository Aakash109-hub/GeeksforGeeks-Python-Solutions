# Array Element Search

## Problem Statement

Given an array `arr` of `n` integers and an integer `x`, determine whether `x` is present in the array. If present, return the index of its first occurrence; otherwise, return `-1`.

### Examples

**Example 1:**
```
Input: arr = [1, 2, 3, 4], x = 3
Output: 2
Explanation: The element 3 is present at index 2.
```

**Example 2:**
```
Input: arr = [10, 8, 30, 4, 5], x = 5
Output: 4
Explanation: The element 5 is present at index 4.
```

**Example 3:**
```
Input: arr = [10, 8, 30], x = 6
Output: -1
Explanation: The element 6 is not present in the array.
```

## Solution Approach

The solution involves a linear search through the array to find the first occurrence of the element `x`.

### Key Steps:

1. **Check Presence**: First, check if the element `x` exists in the array. If not, return `-1` immediately.
2. **Linear Search**: If `x` is present, iterate through the array to find the first occurrence of `x` and return its index.

### Explanation of Each Step:

1. **Check Presence**:
   - The line `if x not in arr` checks if `x` is not present in the array `arr`. If `x` is not found, the function returns `-1` immediately, optimizing the search by avoiding unnecessary iterations.

2. **Linear Search**:
   - If `x` is present in the array, the function proceeds to iterate through each element of the array using a `for` loop.
   - For each element at index `i`, it checks if the element matches `x`. The first occurrence of `x` is found, and its index `i` is returned.

### Example Walkthrough

For `arr = [1, 2, 3, 4]` and `x = 3`:
1. The function checks if `3` is in `[1, 2, 3, 4]`. Since it is, the loop begins.
2. The loop checks each element:
   - `arr[0] = 1` ≠ `3` → continue
   - `arr[1] = 2` ≠ `3` → continue
   - `arr[2] = 3` == `3` → return `2`

For `arr = [10, 8, 30]` and `x = 6`:
1. The function checks if `6` is in `[10, 8, 30]`. Since it is not, the function immediately returns `-1`.

## Time and Space Complexity

- **Time Complexity**: O(n) - In the worst case, the function may need to check every element in the array.
- **Space Complexity**: O(1) - The function uses a constant amount of additional space
