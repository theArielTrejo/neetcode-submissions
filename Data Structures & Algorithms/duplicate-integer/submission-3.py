class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nonDups = set(nums)
        if len(nums) != len(nonDups):
            return True
        return False