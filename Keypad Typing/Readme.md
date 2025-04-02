# Keypad Decimal Representation Converter

## Problem Statement

Given a string `S` of lowercase alphabet characters, convert it into its corresponding decimal representation as found on a standard telephone keypad. Return the concatenated digits as a string.

### Examples

**Example 1:**
```
Input: S = "amazon"
Output: "262966"
Explanation:
'a' → '2'
'm' → '6'
'a' → '2'
'z' → '9'
'o' → '6'
'n' → '6'
Concatenated result: "262966"
```

**Example 2:**
```
Input: S = "hello"
Output: "43556"
Explanation:
'h' → '4'
'e' → '3'
'l' → '5'
'l' → '5'
'o' → '6'
Concatenated result: "43556"
```

## Solution Approach

The solution involves mapping each character in the input string to its corresponding digit on a telephone keypad and then concatenating these digits to form the result.

### Key Steps:

1. **Keypad Mapping**: Create a dictionary that maps each lowercase alphabet character to its corresponding digit as per the standard telephone keypad layout.
2. **Character Conversion**: For each character in the input string, look up its corresponding digit in the dictionary.
3. **Result Construction**: Concatenate all the digits obtained from the previous step to form the final result string.

### Explanation of Each Step:

1. **Keypad Mapping**:
   - The dictionary `keypad_mapping` is defined to hold the mapping of each lowercase alphabet character to its corresponding digit on a telephone keypad. For example, 'a', 'b', and 'c' all map to '2', 'd', 'e', and 'f' map to '3', and so on.

2. **Character Conversion**:
   - For each character in the input string `s`, the corresponding digit is looked up in `keypad_mapping`. This is done using a generator expression inside the `join()` method.

3. **Result Construction**:
   - The digits obtained from the previous step are concatenated into a single string using `''.join()`, which is then returned as the result.

2. **Example Usage**:
   ```python
   print(printNumber("amazon", 6))  # Output: "262966"
   print(printNumber("hello", 5))   # Output: "43556"
   ```
