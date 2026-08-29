class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []
        base = 1
        listlength = 0
        while listlength < len(nums):
            for num in nums:
                base *= num
                #print(base)
            if base != 0:
                products.append(int(base / nums[listlength]))
            else:
            # base == 0 means at least one zero exists
            # if nums[listlength] == 0, then we DO want the product of the rest
                temp = 1
                for i, n in enumerate(nums):
                    if i != listlength:
                        temp *= n
                products.append(temp)
            base = 1
            listlength += 1
            #if listlength > len(nums):
            #    listlength = 0
        return(products)

