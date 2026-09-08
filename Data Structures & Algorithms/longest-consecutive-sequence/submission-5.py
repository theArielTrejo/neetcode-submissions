class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      sortedNums = sorted(set(nums))
      maxConsecutive = 0
      count = 0

      if len(sortedNums) == 0:
        return 0

      nextCurNumber = sortedNums[0]
      for number in sortedNums:
        if nextCurNumber == number:
            nextCurNumber += 1
            count += 1
            maxConsecutive = max(maxConsecutive, count)

        else:
            nextCurNumber = number + 1
            print(nextCurNumber)
            count = 1

      return maxConsecutive
        