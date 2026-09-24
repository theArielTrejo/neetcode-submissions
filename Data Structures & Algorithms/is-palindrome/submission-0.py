class Solution:
    def isPalindrome(self, s: str) -> bool:
        filteredString = "".join(char for char in s if char.isalnum())
        filteredString = filteredString.lower()
        left = 0
        right = len(filteredString) - 1
        while left < right:
            if filteredString[left] != filteredString[right]:
                return False
            left += 1
            right -= 1
        return True