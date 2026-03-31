class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        right = n - 1
        left = 0
        minimum = nums[0]
        min_idx = -1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if minimum > nums[mid]:
                minimum = nums[mid]
                min_idx = mid
                right = mid - 1
            else:
                left = mid + 1
        
        if target <= nums[n - 1]:
            left = min_idx
            right = n - 1
        else:
            right = min_idx - 1
            left = 0
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
            
        
