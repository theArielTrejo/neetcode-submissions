class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        countFreq = {}
        biggestSub = 0

        left = 0
        maxFreq = 0
        for right in range(len(s)):
            countFreq[s[right]] = 1 + countFreq.get(s[right], 0)
            maxFreq = max(countFreq[s[right]], maxFreq)

            while (right - left + 1) - maxFreq > k:
                countFreq[s[left]] -= 1
                left += 1
            biggestSub = max(biggestSub, right - left + 1) 
        return biggestSub
