class Solution:
    def scoreOfString(self, s: str) -> int:
       results = 0
       for char in range(len(s) - 1):
        results += abs(ord(s[char]) - ord(s[char+1]))
       return results