class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ans = [0] * len(nums)
        prod = 1
        zero_occurs = False
        zero_count = 0
        # finding total product without zeros
        for i in nums:
            if i != 0:
                prod *= i
            else:
                zero_occurs = True
                zero_count += 1

        

        if zero_count <= 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    ans[i] = prod
                elif zero_occurs == True:
                    ans[i] = 0
                else:
                    x = prod / nums[i]
                    ans[i] = int(x)

        return ans