class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = set()
        n = len(nums)
        for i in range(n):
            if nums[i] in d:
                return nums[i]
            else:
                d.add(nums[i])