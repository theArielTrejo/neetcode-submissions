class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        prevMap = {}
        # This is similar to two sums for hash
        # but you grab the actual element not index
        for i, n in enumerate(numbers):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff] + 1, i + 1]    
            prevMap[n] = i
            print(prevMap[n])