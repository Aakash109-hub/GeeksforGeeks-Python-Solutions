# Word Character Counter

## Problem Statement

Given a string `S` containing multiple words, count the number of characters in each word and return the counts in order.

### Examples

**Example 1:**
```
Input: S = "the quick brown fox"
Output: [3, 5, 5, 3]
Explanation: 
- "the" has 3 characters
- "quick" has 5 characters
- "brown" has 5 characters
- "fox" has 3 characters
```

**Example 2:**
```
Input: S = "geeks for geeks"
Output: [5, 3, 5]
Explanation:
- "geeks" has 5 characters
- "for" has 3 characters
- "geeks" has 5 characters
```

## Solution Approach

The solution involves splitting the input string into individual words and then counting the characters in each word.

### Key Steps:

1. **Split the String**: Split the input string into a list of words using the `split()` method, which by default splits on whitespace.
2. **Count Characters**: Iterate over each word in the list and count the number of characters using the `len()` function.
3. **Return the Counts**: Store the counts in a list and return it.

### Explanation of Each Step:

1. **Splitting the String**:
   - `s.split()` splits the string `s` into a list of words based on whitespace. For example, `"the quick brown fox"` becomes `["the", "quick", "brown", "fox"]`.

2. **Counting Characters**:
   - We initialize an empty list `count` to store the character counts of each word.
   - For each word in the list `split_word`, we calculate its length using `len(word)` and append this value to `count`.

3. **Returning the Result**:
   - The list `count` now contains the character counts of each word in the order they appeared in the input string. This list is returned as the result.

### Example Walkthrough

For `S = "the quick brown fox"`:
1. After splitting, `split_word` becomes `["the", "quick", "brown", "fox"]`.
2. The lengths of these words are `3, 5, 5, 3`, respectively.
3. The function returns `[3, 5, 5, 3]`.

For `S = "geeks for geeks"`:
1. After splitting, `split_word` becomes `["geeks", "for", "geeks"]`.
2. The lengths of these words are `5, 3, 5`, respectively.
3. The function returns `[5, 3, 5]`.

## How to Use

1. **Function Call**:
   - The function `countChars(s)` can be called with a string `s` containing multiple words.
   - It returns a list of integers representing the number of characters in each word, in the order they appear in the input string.

2. **Example Usage**:
   ```python
   print(countChars("the quick brown fox"))  # Output: [3, 5, 5, 3]
   print(countChars("geeks for geeks"))      # Output: [5, 3, 5]
   ```
