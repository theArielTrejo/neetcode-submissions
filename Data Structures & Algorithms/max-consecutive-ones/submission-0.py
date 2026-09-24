class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxcount = 0
        currentcount = 0
        for i in nums:
            if i == 1:
                currentcount += 1
                maxcount = max(maxcount, currentcount)
            else:
                currentcount = 0
        return maxcount