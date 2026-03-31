class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            if i not in seen: # if the number not already in the set -> add to set
                seen.add(i)
            else:
                return True # runs if there is duplicate
        
        return False