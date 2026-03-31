class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        answer = []
        for i in range(len(nums)):
            if (target - nums[i]) not in seen:
                seen[nums[i]] = i
            else:
                answer.append(seen[target-nums[i]])
                answer.append(i)
        
        return answer