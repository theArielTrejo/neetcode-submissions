class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      left = 0
      right = 1
      maxMoney = 0
      while right < len(prices):
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            maxMoney = max(maxMoney, profit)
        else:
            left = right
        right += 1
      return maxMoney
