class Solution:
    def maxArea(self, heights: List[int]) -> int:
      left = 0
      right = len(heights) - 1
      themax = 0
      while left < right:
        area = min(heights[left], heights[right]) * (right - left)
        themax = max(themax, area)
        if heights[left] <= heights[right]:
            left += 1
        else:
            right -= 1
      return themax
