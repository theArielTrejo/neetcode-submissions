class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT = {}
        window = {}
        for char in t:
            # countT.get(char, 0)
            # ^ This grabs char and freq,
            # If no freq it sets it to 0
            countT[char] = 1 + countT.get(char, 0)

        have = 0
        need = len(countT)
        results = [-1, 1]
        resultsLen = float("infinity")
        left = 0
        for right in range(len(s)):
            char = s[right]
            window[char] = 1 + window.get(char, 0)

            if char in countT and window[char] == countT[char]:
                have += 1
            while have == need:
                if (right - left + 1 ) < resultsLen:
                    results = [left, right]
                    resultsLen = right - left + 1

                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1
        left, right = results
        return s[left : right + 1] if resultsLen != float("infinity") else ""