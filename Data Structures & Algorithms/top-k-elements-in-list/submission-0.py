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
        # This below grabs the keys of the largest k elements.
        # key = completed.get grabs the value of that key
        # For example, k = 2, this means grab two largest keys
        # completed.get(2) -> would give you the value, lets say 10
        # 2 had a frequency of 10 2:10
        biggest = heapq.nlargest(k, completed, key=completed.get)
        return biggest