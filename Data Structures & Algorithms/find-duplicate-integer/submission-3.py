class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        size = len(nums)
        n = size - 1

        a = 0
        b = 0
        while 1:
            a = nums[a]
            b = nums[nums[b]]
            if a == b:
                break
        
        c = 0
        while 1:
            c = nums[c]
            a = nums[a]
            if a == c:
                return a