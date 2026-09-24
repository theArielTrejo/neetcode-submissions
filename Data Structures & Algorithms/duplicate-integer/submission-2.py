class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dups = set()
        dups.update(nums)
        if len(dups) != len(nums):
            return True
        return False