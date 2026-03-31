class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        leftc, leftr = 0, 0
        rightr, rightc = len(matrix[0]) - 1, len(matrix) - 1

        # binary search for the row and then binary search within the row for the index
        while leftc <= rightc:
            # calc mid row
            midr = (leftc + rightc) // 2
            # if target in current row
            if matrix[midr][leftr] <= target and matrix[midr][rightr] >= target:
                # search row
                while leftr <= rightr:
                    midc = (leftr + rightr) // 2
                    if target == matrix[midr][midc]:
                        return True
                    elif target > matrix[midr][midc]:
                        leftr = midc + 1
                    else:
                        rightr = midc - 1

            # where the target is in a lower row
            elif matrix[midr][leftr] > target:
                rightc = midr - 1
            # where the target is in a higher row
            elif matrix[midr][rightr] < target:
                leftc = midr + 1

        return False