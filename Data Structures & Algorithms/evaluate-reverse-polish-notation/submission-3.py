class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']

        for c in tokens:
            # if a given character is not an operator
            if c not in operators:
                stack.append(c)
            else:
                second = int(stack.pop())
                first = int(stack.pop())
                if c == '+':
                    stack.append(first + second)
                elif c == '-':
                    stack.append(first - second)
                elif c == '*':
                    stack.append(first * second)
                else:
                    stack.append(first / second)
        
        return int(stack.pop())