class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n =  len(matrix[0])
        if n == 0:
            return False
        left = 0
        right =  (m * n) - 1
        while left <= right:
            mid = (left + right)//2
            row = (mid //n)
            column = mid - (row * n)
            if matrix[row][column] == target:
                return True
            elif matrix[row][column] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False