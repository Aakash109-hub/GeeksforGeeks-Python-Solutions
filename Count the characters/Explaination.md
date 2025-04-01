# Character Occurrence Counter

## Problem Statement

Given a string `S`, count the characters that have exactly `N` occurrences. If a character appears consecutively, it should be counted as a single occurrence.

### Examples

**Example 1:**
```
Input: S = "abc", N = 1
Output: 3
Explanation: 'a', 'b' and 'c' all appear exactly once.
```

**Example 2:**
```
Input: S = "geeksforgeeks", N = 2
Output: 4
Explanation: 'g', 'e', 'k' and 's' each appear exactly twice when consecutive duplicates are counted as one.
```

## Solution Approach

The solution involves processing the input string to count character occurrences while treating consecutive duplicates as a single occurrence, then counting how many characters meet the specified occurrence count `N`.

### Key Steps:

1. **Process the String**: First, we process the string to collapse consecutive duplicate characters into single characters. For example, "geeksforgeeks" becomes "geksforgeks".

2. **Count Occurrences**: We then count how many times each character appears in this processed string.

3. **Check Against N**: Finally, we count how many characters have exactly `N` occurrences in the processed string.

### Explanation of Each Step:

1. **Processing the String**:
   - `groupby(S)` from the `itertools` module groups consecutive identical characters together.
   - `''.join(char for char, _ in groupby(S))` joins the first character of each group, effectively removing consecutive duplicates.

2. **Counting Occurrences**:
   - We initialize an empty dictionary `d` to keep track of character counts.
   - For each character in the processed string, we increment its count in the dictionary.

3. **Checking Occurrence Count**:
   - We iterate through the values in the dictionary (which represent the occurrence counts of each character).
   - For each value that matches `N`, we increment our result counter.

### Example Walkthrough

For `S = "geeksforgeeks"` and `N = 2`:
1. After processing, the string becomes `"geksforgeks"`.
2. The occurrence counts are:
   - 'g': 2, 'e': 2, 'k': 2, 's': 2, 'f': 1, 'o': 1, 'r': 1
3. Characters with exactly 2 occurrences: 'g', 'e', 'k', 's' → Total count = 4.

## How to Use

1. **Function Call**:
   - The function `getCount(S, N)` can be called with a string `S` and an integer `N`.
   - It returns the count of characters in `S` that appear exactly `N` times (with consecutive duplicates counted as one).

2. **Example Usage**:
   ```python
   print(getCount("abc", 1))  # Output: 3
   print(getCount("geeksforgeeks", 2))  # Output: 4
   ```

## Dependencies

- The code uses the `groupby` function from Python's `itertools` module, which is part of the standard library. No additional installations are required.
