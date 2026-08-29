class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nondups = set(nums)
        if len(nondups) == len(nums):
            return False
        else:
            return True