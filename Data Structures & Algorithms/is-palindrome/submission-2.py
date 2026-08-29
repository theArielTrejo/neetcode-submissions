class Solution:
    def isPalindrome(self, s: str) -> bool:
        modified_s = "".join(char for char in s.lower() if char.isalnum())
        reverse_s = modified_s[::-1]
        if modified_s == reverse_s:
            return True
        else:
            return False