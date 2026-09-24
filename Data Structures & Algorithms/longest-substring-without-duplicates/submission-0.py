class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subSets = set()
        left = 0
        maxSub = 0
        for right in range(len(s)):
            while s[right] in subSets:
                subSets.remove(s[left])
                left += 1
            subSets.add(s[right])
            maxSub = max(maxSub, right - left + 1)
        return maxSub