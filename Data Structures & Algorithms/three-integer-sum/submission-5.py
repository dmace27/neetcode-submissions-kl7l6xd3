class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        answer_set = set()
        n = len(nums)
        # sort array
        for i1 in range(n):
            for i2 in range(i1+1, n):
                if nums[i1] > nums[i2]:
                    temp = nums[i1]
                    nums[i1] = nums[i2]
                    nums[i2] = temp

        for k in range(n):
            i = k + 1
            j = n - 1
            while i < j:
                # if a solution is found
                if nums[i] + nums[j] == -nums[k]:
                    s = [nums[k], nums[i], nums[j]]
                    ts = tuple(s)
                    if ts not in answer_set:
                        answer_set.add(ts)
                        ans.append(s)
                
                # logic for updating the pointers
                if nums[i] + nums[j] >= -nums[k]:
                    j -= 1
                elif nums[i] + nums[j] < -nums[k]:
                    i += 1

        return ans



            
