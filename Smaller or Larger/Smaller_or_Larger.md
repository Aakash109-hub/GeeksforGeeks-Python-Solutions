# Smaller and Larger Problem

## Problem Statement
Given a **sorted array** `arr` and a target value `target`, return an array of size 2 where:
- The **first value** is the count of elements **less than or equal** to `target`.
- The **second value** is the count of elements **greater than or equal** to `target`.

### Examples
```python
Input:  arr = [1, 2, 8, 10, 11, 12, 19], target = 0
Output: (0, 7)  
# Explanation: No elements ≤ 0, all 7 elements ≥ 0.

Input:  arr = [1, 5, 8, 12, 12, 12, 19], target = 12
Output: (6, 4)  
# Explanation: 6 elements ≤ 12, 4 elements ≥ 12.
```

---

## Approaches

### 1. Linear Scan (Brute Force)
- **Time Complexity**: O(n)  
- **Space Complexity**: O(1)  
- **Idea**: Iterate through each element in the array and count how many are `≤ target` and `≥ target`.

### 2. Binary Search (Optimized for Sorted Arrays)
- **Time Complexity**: O(log n)  
- **Space Complexity**: O(1)  
- **Idea**: Use `bisect` to find the insertion points:
  - `bisect_right` gives the count of elements `≤ target`.
  - `bisect_left` gives the starting index of elements `≥ target`.

---
## Explanation
1. **Linear Scan**:
   - Initialize counters `a` and `b` to zero.
   - For each element in `arr`:
     - Increment `a` if the element is `≤ target`.
     - Increment `b` if the element is `≥ target`.
   - Return the tuple `(a, b)`.

2. **Binary Search**:
   - Use `bisect_right` to find the index where `target` would be inserted to maintain order (counts elements `≤ target`).
   - Use `bisect_left` to find the first occurrence of `target` (calculates elements `≥ target` as `len(arr) - bisect_left`).

---

## How to Use
1. Save the code in a file (e.g., `smaller_and_larger.py`).
2. Import the function and call it with your input:
```python
from smaller_and_larger import getMoreAndLess

arr = [1, 5, 8, 12, 12, 12, 19]
target = 12
print(getMoreAndLess(arr, target))  # Output: (6, 4)
```

---

## Notes
- The **linear scan** works for any array (sorted or unsorted).
- The **binary search** approach is optimal for sorted arrays (O(log n) vs. O(n)).
