# Given a string s consisting of words and spaces,
# return the length of the last word in the string.

# Example 1

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1

        while i >= 0 and s[i] == ' ':
            i -= 1
        lastIndex = i
        while i >= 0 and s[i] != ' ':
            i -= 1

        return lastIndex - i


# <--------------------------------------------->

# Example 2

class Solution2:
    def lengthOfLastword2(self, s: str) -> int:
        last_len = 0
        curr_len = 0

        for letter in s:
            if letter == " ":
                if curr_len != 0:
                    last_len = curr_len
                curr_len = 0
            else:
                curr_len += 1
        if curr_len != 0:
            last_len = curr_len

        return last_len
