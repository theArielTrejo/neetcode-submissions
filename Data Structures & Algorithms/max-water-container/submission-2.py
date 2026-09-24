class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        left = 0
        right = len(heights) - 1
        length = 0
        width = 0
        while left < right:
            length = right - left
            width = min(heights[left], heights[right])
            area = length * width
            maxArea = max(maxArea, area)
            if heights[left] < heights[right] or heights[left] == heights[right]:
                left += 1
            else:
                right -= 1
        return maxArea