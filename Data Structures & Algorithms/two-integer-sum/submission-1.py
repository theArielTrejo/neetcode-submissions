class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, val in enumerate(nums):
           missingNum = target - val
           if missingNum in seen:
            return [seen[missingNum], i]
           seen[val] = i 