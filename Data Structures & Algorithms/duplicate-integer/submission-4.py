class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       nonDups = set(nums)
       if len(nonDups) != len(nums):
        return True
       return False