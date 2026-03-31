class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        fre = {}
        buckets = {}
        for i in nums:
            if i not in fre:
                fre[i] = 1
            else:
                fre[i] += 1
        
        for i in fre:
            if fre[i] not in buckets:
                buckets[fre[i]] = []
            
            buckets[fre[i]].append(i)
        
        count = 0
        for i in range(len(nums), 0, -1):
            if i in buckets:
                for j in buckets[i]:
                    ans.append(j)
                    count += 1
                    if count == k:
                        return ans
        

        return ans
