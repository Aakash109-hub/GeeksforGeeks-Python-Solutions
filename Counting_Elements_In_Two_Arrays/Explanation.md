# Counting Elements in Two Arrays

## Problem Statement

Given two unsorted arrays `a[]` and `b[]` (which may contain duplicates), count how many elements in `b[]` are less than or equal to each element in `a[]`.

### Examples

**Example 1:**
```python
Input: a = [1, 2, 3, 4, 7, 9], b = [0, 1, 2, 1, 1, 4]
Output: [4, 5, 5, 6, 6, 6]
```
Explanation:
- For a[0] = 1, there are 4 elements in b (0, 1, 1, 1) ≤ 1
- For a[1] = 2, there are 5 elements in b (0, 1, 1, 1, 2) ≤ 2
- For a[2] = 3, there are 5 elements in b ≤ 3
- For a[3] = 4, there are 6 elements in b ≤ 4
- For a[4] = 7 and a[5] = 9, there are 6 elements in b ≤ each

**Example 2:**
```python
Input: a = [4, 8, 7, 5, 1], b = [4, 48, 3, 0, 1, 1, 5]
Output: [5, 6, 6, 6, 3]
```

**Example 3:**
```python
Input: a = [10, 20], b = [30, 40, 50]
Output: [0, 0]
```

## Solution Approach

The efficient solution involves:
1. Sorting array `b` to enable binary search
2. For each element in `a`, use binary search to find how many elements in `b` are ≤ it
3. The `bisect_right` function from Python's bisect module helps find the insertion point which gives us the count

## Code Explanation

1. **Sorting**: First, we sort array `b` to enable efficient binary search operations.
2. **Binary Search**: For each element `num` in array `a`, we use `bisect_right` to find:
   - The rightmost position where `num` would be inserted to keep `b` sorted
   - This position equals the count of elements in `b` that are ≤ `num`
3. **Result Construction**: We collect all counts in a result list and return it

### Time Complexity
- Sorting `b`: O(m log m) where m is length of `b`
- Binary searches for all elements in `a`: O(n log m) where n is length of `a`
- **Total**: O((m + n) log m)

### Space Complexity
- O(1) additional space (excluding input/output storage)
