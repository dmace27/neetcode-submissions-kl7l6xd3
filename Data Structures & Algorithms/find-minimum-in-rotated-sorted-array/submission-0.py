class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        right = n - 1
        left = 0
        minimum = nums[0]

        while left <= right:
            mid = (left + right) // 2
            if minimum > nums[mid]:
                minimum = nums[mid]
                right = mid - 1
            else:
                left = mid + 1
        
        return minimum