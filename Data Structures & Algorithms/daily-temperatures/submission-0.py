class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []
        # add first value to stack
        stack.append(0)
        for i in range(1, n):
            # the values in the stack are days that are still waiting for a higher temp
            # in the case the monotonic condition breaks
            while stack and temperatures[stack[-1]] < temperatures[i]:
                result[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return result