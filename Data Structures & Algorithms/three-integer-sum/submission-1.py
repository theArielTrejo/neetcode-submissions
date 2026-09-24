class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
      nums = sorted(nums)
      triplets = []
      for i, val in enumerate(nums):
        if val > 0:
            break
        if i > 0 and val == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1
        while left < right:
            threeSum = val + nums[left] + nums[right]
            if threeSum > 0:
                right -= 1
            elif threeSum < 0:
                left += 1
            else:
                triplets.append([val, nums[left], nums[right]])
                left += 1
                right -= 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
      return triplets
