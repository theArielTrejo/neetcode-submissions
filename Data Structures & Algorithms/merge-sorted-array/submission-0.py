class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        removeItems = len(nums1) - m
        while removeItems != 0:
            nums1.pop(-1)
            removeItems -= 1
        for i in range(n):
            nums1.append(nums2[i])
        nums1.sort()
        
        