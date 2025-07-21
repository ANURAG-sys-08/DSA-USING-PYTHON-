# Count words in a string

# You are given a string s. Your task is to count the number of words in the string and return the total count. A word is defined as a sequence of characters separated by spaces.

# Example:

# Input: "Hello, World!"
# Output: 2
 
# Input: "Python programming is fun."
# Output: 4

def count_words(s):
    count = 0
    in_word = False
    
    for i in range(len(s)):
        if s[i] != ' ':
            if not in_word:
                count += 1
                in_word = True
        else:
            in_word = False

    return count

# Test
print(count_words("hello  world")) 