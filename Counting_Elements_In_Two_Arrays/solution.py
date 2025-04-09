from bisect import bisect_right

class Solution:
    def countEleLessThanOrEqual(self, a, b):
        b.sort()
        result = []
        # For each element in a, find count using binary search
        for num in a:
            count = bisect_right(b, num)  # Get the position of first element > num
            result.append(count)
        return result
