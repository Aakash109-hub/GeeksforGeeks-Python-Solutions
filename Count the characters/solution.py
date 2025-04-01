from itertools import groupby

def getCount(self, S, N):
    # Step 1: Process the string to collapse consecutive duplicates
    processed_string = ''.join(char for char, _ in groupby(S))
    
    # Step 2: Count occurrences of each character in the processed string
    d = {}
    for char in processed_string:
        d[char] = d.get(char, 0) + 1
    
    # Step 3: Count how many characters have exactly N occurrences
    count = 0
    for value in d.values():
        if value == N:
            count += 1
    
    return count
