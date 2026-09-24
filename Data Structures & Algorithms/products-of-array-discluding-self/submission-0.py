class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        placeholder = 0
        productlist = []
        while placeholder < len(nums):
            productNum = 1
            for i, val in enumerate(nums):
                if i == placeholder:
                    continue
                productNum = val * productNum
            productlist.append(productNum)
            placeholder += 1
        return productlist

