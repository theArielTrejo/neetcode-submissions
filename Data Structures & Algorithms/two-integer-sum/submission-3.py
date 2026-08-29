class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        findNum = 0
        found = {} # This is a dict
        for i, j in enumerate(nums):
            findNum = target - j
            if findNum in found:
                return [found[findNum], i]
            found[j] = i
