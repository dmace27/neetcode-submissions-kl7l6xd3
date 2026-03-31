class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        for i in range(len(heights)):
            l = i - 1
            r = i + 1
            stack = []
            stack.append(i)
            # probe left
            while l >= 0:
                if heights[l] >= heights[i]:
                    stack.append(l)
                else:
                    break
                l -= 1
            # probe right
            while r < len(heights):
                if heights[r] >= heights[i]:
                    stack.append(r)
                else:
                    break
                r += 1

            if area < len(stack) * heights[i]:
                area = len(stack) * heights[i]



        return area