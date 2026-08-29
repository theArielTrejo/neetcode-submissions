import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        amountofnums = {}
        for num in nums:
            if num in amountofnums:
                amountofnums[num] += 1
            else:
                amountofnums[num] = 1
        biggest = heapq.nlargest(k, amountofnums, key=amountofnums.get)
        return biggest
        