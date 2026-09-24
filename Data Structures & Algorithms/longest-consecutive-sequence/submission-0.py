class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nonDups = set(nums)
        highestLen = 0

        for value in nonDups:
            if value - 1 not in nonDups:
                length = 1
                currentVal = value
                while currentVal + 1 in nonDups:
                    length += 1
                    currentVal += 1
                highestLen = max(highestLen, length)
        return highestLen