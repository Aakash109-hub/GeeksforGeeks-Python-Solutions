def count_digit_occurrence(k, arr):
    total = 0
    for num in arr:
        n = abs(num)  # Handle negative numbers
        while n > 0:
            if n % 10 == k:
                total += 1
            n //= 10
    return total
