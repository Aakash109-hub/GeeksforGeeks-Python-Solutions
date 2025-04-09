# Array Subset Problem

## Problem Statement

Given two arrays `a[]` and `b[]`, determine whether `b[]` is a subset of `a[]`. This means every element in `b[]` must be present in `a[]` with at least the same frequency.

### Examples

**Example 1:**
```python
Input: a = [11, 7, 1, 13, 21, 3, 7, 3], b = [11, 3, 7, 1, 7]
Output: True
```
Explanation: All elements of b appear in a with sufficient counts (two 7s in b, two 7s in a)

**Example 2:**
```python
Input: a = [1, 2, 3, 4, 4, 5, 6], b = [1, 2, 4]
Output: True
```
Explanation: All elements of b appear in a (note the two 4s in a cover one 4 in b)

**Example 3:**
```python
Input: a = [10, 5, 2, 23, 19], b = [19, 5, 3]
Output: False
```
Explanation: 3 is not present in a, so b is not a subset

## Solution Approach

The solution uses a two-pointer technique after sorting both arrays:
1. Sort both arrays to enable ordered comparison
2. Use two pointers to traverse both arrays:
   - If elements match, move both pointers forward
   - If a's element is smaller, move only a's pointer
   - If b's element is smaller (not found in a), return False
3. If we reach end of b, it's a subset; otherwise not

## Code Explanation

1. **Sorting**: Both arrays are sorted to enable the two-pointer comparison
2. **Two-pointer traversal**:
   - Pointer `i` tracks position in `a`, `j` in `b`
   - If `a[i] < b[j]`: Move `i` forward (current a element too small)
   - If `a[i] == b[j]`: Move both forward (match found)
   - If `a[i] > b[j]`: Return False (element in b not found in a)
3. **Termination check**: If we exhaust `b` (`j == len(b)`), it's a subset

### Time Complexity
- Sorting: O(n log n + m log m) where n,m are lengths of a,b
- Two-pointer traversal: O(n + m)
- **Total**: O(n log n + m log m)

### Space Complexity
- O(1) additional space (sorting may use O(n) or O(1) depending on sort implementation)
