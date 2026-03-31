class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(speed)
        num_fleets = 0
        stack = []
        def cycles(idx: int) -> int:
            return (target - position[idx]) / speed[idx]
             
        #sort by position
        for i in range(n - 1):
            swapped = False
            for j in range(0, n - i - 1):
                # Compare adjacent positions
                if position[j] < position[j + 1]:
                    position[j], position[j + 1] = position[j + 1], position[j]
                    speed[j], speed[j + 1] = speed[j + 1], speed[j]
                    
                    swapped = True
            if not swapped:
                break

        # add first car to stack
        stack.append(0)
        for i in range(1, n):
            if stack and cycles(stack[-1]) < cycles(i):
                stack.append(i)

        for i in range(len(stack)):
            num_fleets += 1
        
        return num_fleets


                