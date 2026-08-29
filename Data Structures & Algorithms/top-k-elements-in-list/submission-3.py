import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # heapq
        freqmap = {}
        count = 0
        for i in nums:
            if i in freqmap:
                freqmap[i] += 1
            else:
                freqmap[i] = 1
        biggest = heapq.nlargest(k, freqmap, key=freqmap.get)
        return biggest
