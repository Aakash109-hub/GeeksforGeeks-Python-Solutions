# Replace all 0's with 5

## Problem Statement
You are given an integer `n`. You need to convert all zeroes of `n` to 5.

### Examples:
**Input:**  
n = 1004  
**Output:**  
1554  
**Explanation:**  
There are two zeroes in 1004. On replacing all zeroes with 5, the new number becomes 1554.

**Input:**  
n = 121  
**Output:**  
121  
**Explanation:**  
Since there are no zeroes in 121, the number remains unchanged.

## Solution Approach
The solution involves:
1. Converting the integer to a string to easily manipulate each digit
2. Using the string's `replace()` method to replace all '0' characters with '5'
3. Converting the result back to an integer before returning

### Time Complexity
The time complexity is O(d), where d is the number of digits in the input number. This is because:
- Converting the number to a string takes O(d) time
- The replace operation scans the string once, taking O(d) time
- Converting back to an integer takes O(d) time

### Space Complexity
The space complexity is O(d) as we create a new string representation of the number.
