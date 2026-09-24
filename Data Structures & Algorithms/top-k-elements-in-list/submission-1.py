import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seenNums = {}
        for freq in nums:
            if freq in seenNums:
                seenNums[freq] += 1
            else:
                seenNums[freq] = 1
        biggest = heapq.nlargest(k, seenNums, key=seenNums.get)
        return biggest    