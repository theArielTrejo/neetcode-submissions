class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Use isalum for only letters and numbers
        # Use isalpha for only letters
        alphanumsonly = ''.join([char for char in s if char.isalnum()])
        forwards = alphanumsonly.lower()
        backwards = forwards[::-1]
        print(forwards)
        print(backwards)
        # This works by removing all symbols & spaces + making all letters lowercase
        # Then you store the modified string reversed and then compare
        if forwards == backwards:
            return True
        else:
            return False