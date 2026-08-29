class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = "" # Stores encoded string
        # The word gets encoded by add the length of the string
        # Followed by a pound symbol
        for s in strs:
            encoded += str(len(s)) + '#' + s
        return encoded

    def decode(self, s: str) -> List[str]:
            reset = []
            i = 0
            while i < len(s):
                j = i
                # 1. Read length until hitting "#"
                while s[j] != "#":
                    j += 1
                length = int(s[i:j]) # convert length substring to int
                j += 1   # move past "#"

                 # 2. Extract the actual string of that length
                word = s[j : j + length]
                reset.append(word)

                # 3. Move to the next encoded segment
                i = j + length
            return reset