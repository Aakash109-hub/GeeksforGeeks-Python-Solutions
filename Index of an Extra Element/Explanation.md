# Index of Extra Element in Sorted Arrays

## Problem Statement

Given two sorted arrays `arr1` and `arr2` of distinct elements where `arr1` contains all elements of `arr2` plus one extra element, find the index of the extra element in `arr1`.

### Examples

**Example 1:**
```
Input: 
arr1 = [2,4,6,8,9,10,12]
arr2 = [2,4,6,8,10,12]
Output: 4
Explanation: The extra element is 9 at index 4 in arr1.
```

**Example 2:**
```
Input:
arr1 = [3,5,7,8,11,13]
arr2 = [3,5,7,11,13]
Output: 3
Explanation: The extra element is 8 at index 3 in arr1.
```

**Example 3:**
```
Input:
arr1 = [3,5]
arr2 = [3]
Output: 1
Explanation: The extra element is 5 at index 1 in arr1.
```

## Solution Approach

The solution involves comparing elements of both arrays at each index until a mismatch is found. The index where the first mismatch occurs is the index of the extra element.

### Key Steps:

1. **Iterate through arrays**: Compare elements of `arr1` and `arr2` at each index.
2. **Find mismatch**: The first index where elements differ is the index of the extra element.
3. **Handle edge case**: If all compared elements match, the extra element must be at the last index of `arr1`.

### Explanation of Each Step:

1. **Initialization**:
   - `n` is set to the length of the smaller array `arr2`.

2. **Element Comparison**:
   - The loop runs from `0` to `n-1` (inclusive).
   - At each index `i`, elements `arr1[i]` and `arr2[i]` are compared.
   - If they differ, `i` is returned immediately as it's the index of the extra element.

3. **Edge Case Handling**:
   - If the loop completes without finding any mismatch, the extra element must be at index `n` (the last position of `arr1`), which is returned.

### Example Walkthrough

For `arr1 = [2,4,6,8,9,10,12]` and `arr2 = [2,4,6,8,10,12]`:
1. Compare elements at each index:
   - Index 0: 2 == 2 → continue
   - Index 1: 4 == 4 → continue
   - Index 2: 6 == 6 → continue
   - Index 3: 8 == 8 → continue
   - Index 4: 9 ≠ 10 → return 4

For `arr1 = [3,5]` and `arr2 = [3]`:
1. Compare elements:
   - Index 0: 3 == 3 → continue
   - Loop ends → return `n` (1)

## Time and Space Complexity

- **Time Complexity**: O(n) - In the worst case, we may need to compare all elements of the smaller array.
- **Space Complexity**: O(1) - The algorithm uses constant extra space.
