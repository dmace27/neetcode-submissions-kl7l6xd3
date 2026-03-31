class Solution:
    def trap(self, height: List[int]) -> int:
            
        area = 0
        n = len(height)
        i = 0
        j = n - 1
        left = [0] * n
        right = [0] * n
        current_right = 0
        current_left = 0
        # makes an array of the biggest value to the left of a given index
        for i in range(n):
            left[i] = current_left
            if height[i] > current_left:
                current_left = height[i]

        # makes an array of the biggest value to the right of a given index
        for i in range(n-1, 0, -1):
            right[i] = current_right
            if height[i] > current_right:
                current_right = height[i]

        for i in range(n):
            # if rain water is able to be trapped
            if right[i] > height[i] and left[i] > height[i]:
                # the amount trapped is based on the lesser of the two biggest numbers
                if right[i] > left[i]:
                    area += (left[i] - height[i])
                elif right[i] <= left[i]:
                    area += (right[i] - height[i])
        
        return area