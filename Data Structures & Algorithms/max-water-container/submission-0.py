class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        n = len(heights)
        i = 0
        j = n-1

        while i < j:
            area = (j - i)
            if heights[i] > heights[j]:
                area *= heights[j]
            else:
                area *= heights[i]

            if area > max_area:
                max_area = area
            
            # logic for moving pointers
            # want to get rid of the smaller number
            if heights[i] > heights[j]:
                j -= 1
            elif heights[j] > heights[i]:
                i +=1
            else:
                if heights[j-1] > heights[i+1]:
                    j -= 1
                else:
                    i += 1
                
            
        return max_area