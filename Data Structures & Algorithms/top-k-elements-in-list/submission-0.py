from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        completed = {}

        for freq in nums:
            if freq in completed:
                completed[freq] += 1
            else:
                completed[freq] = 1
        biggest = heapq.nlargest(k, completed, key=completed.get)
        return biggest