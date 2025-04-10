# Finding K Largest Elements in an Array

## Problem Statement

Given an array of positive integers and an integer `k`, return the `k` largest elements in decreasing order.

### Examples

**Example 1:**
```python
Input: arr = [12, 5, 787, 1, 23], k = 2
Output: [787, 23]
```
Explanation: The two largest elements are 787 and 23.

**Example 2:**
```python
Input: arr = [1, 23, 12, 9, 30, 2, 50], k = 3
Output: [50, 30, 23]
```
Explanation: The three largest elements are 50, 30, and 23.

**Example 3:**
```python
Input: arr = [12, 23], k = 1
Output: [23]
```
Explanation: The largest element is 23.

## Solution Approach

The straightforward solution involves:
1. Sorting the array in descending order
2. Taking the first `k` elements from the sorted array

## Code Explanation

1. **Sorting**: The array is sorted in descending order using `sort(reverse=True)`
2. **Slicing**: The first `k` elements are returned using array slicing `arr[:k]`

### Time Complexity
- Sorting: O(n log n) where n is the length of the array
- Slicing: O(k)
- **Total**: O(n log n) (dominated by sorting)

### Space Complexity
- O(1) additional space (sorting is in-place)
