class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        m = 0
        for i in piles:
            if m < i:
                m = i

        left = 1
        right = m
        result = m
        while left <= right:
            mid = (left + right) // 2
            
            # check if current mid is feasible
            cycles = 0
            for i in range(n):
                cycles += (piles[i] + mid - 1) // mid
            if cycles > h:
                left = mid + 1
            else:
                result = mid
                right = mid - 1

        return result










          