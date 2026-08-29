class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}
        for index, value in enumerate(nums):
            thegoal = target - value
            if thegoal in sums:
                return [sums[thegoal], index]
            sums[value] = index
            