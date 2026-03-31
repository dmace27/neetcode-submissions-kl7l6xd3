class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {']': '[', ')': '(', '}': '{'}

        for c in s:
            # if a given character is a close bracket
            if c in d:
                if stack and stack[-1] == d[c]:
                    stack.pop()
                else:
                    return False
            # if a given character is an open bracket
            else:
                stack.append(c)


        return True if not stack else False