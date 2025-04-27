def convertFive(n):
    """
    Function to replace all 0's with 5 in given integer n
    
    Args:
    n (int): Input number
    
    Returns:
    int: Number with all 0's replaced by 5's
    """
    a = str(n)
    return int(a.replace("0", "5"))

# Example usage:
if __name__ == "__main__":
    test_cases = [1004, 121, 10304, 0, 98765]
    for num in test_cases:
        print(f"Input: {num} => Output: {convertFive(num)}")
