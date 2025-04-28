# Count Occurrence of Digit `k` in Array

## Problem Statement
Given an array `arr` and a digit `k` (0 ≤ `k` ≤ 9), return the total number of times `k` appears across all numbers in the array.

### Examples
```python
Input:  k=1, arr = [11, 12, 13, 14, 15]
Output: 6  
# Explanation: Digit '1' appears in 11 (twice), 12 (once), 13 (once), 14 (once), and 15 (once). Total = 6.

Input:  k=3, arr = [11, 121, 15]
Output: 0  
# Explanation: Digit '3' does not appear in any number.
```

---

## Approach
1. **Convert `k` to a string** for easy comparison.
2. **Iterate through each number** in the array:
   - Convert the number to a string.
   - Count occurrences of `k` in the string representation of the number.
3. **Sum the counts** across all numbers.

### Time Complexity
- **O(n * d)**, where `n` is the number of elements in the array and `d` is the average number of digits per element.

### Space Complexity
- **O(1)**, no additional space is used beyond input and counters.

---

### Explanation
1. **Convert `k` to a string** (`k_str`) to facilitate digit comparison.
2. **Initialize `total` counter** to zero.
3. **Loop through each number** in `arr`:
   - Convert the number to a string.
   - Use `str.count(k_str)` to count occurrences of `k` in the number.
   - Add the count to `total`.
4. **Return `total`**.

---

## How to Use
1. Save the code in a file (e.g., `count_digit_occurrence.py`).
2. Import and call the function:
```python
from count_digit_occurrence import count_digit_occurrence

k = 1
arr = [11, 12, 13, 14, 15]
print(count_digit_occurrence(k, arr))  # Output: 6
```

## Edge Cases
- **`k` not in any number**: Returns `0` (e.g., `k=3`, `arr=[11, 121]`).
- **Empty array**: Returns `0`.
- **`k` appears multiple times in a single number** (e.g., `k=1`, `arr=[111]` → `3`).
