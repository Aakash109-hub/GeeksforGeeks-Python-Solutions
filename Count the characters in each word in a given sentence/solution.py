def countChars(self, s):
    # Step 1: Split the string into words
    split_word = s.split()
    
    # Step 2: Count characters in each word
    count = []
    for word in split_word:
        count.append(len(word))
    
    # Step 3: Return the list of counts
    return count
