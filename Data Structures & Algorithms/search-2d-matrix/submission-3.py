class Solution:

    def calculateCoords(self, index) -> tuple[int, int]:
        return index // self.cols, index % self.cols

    def binarySearch(self, nums, left, right, target) -> bool:

        if left > right:
            return False

        middle = (left + right) // 2

        x, y = self.calculateCoords(middle)
            
        if target == nums[x][y]:
            return True
        elif target < nums[x][y]:
            return self.binarySearch(nums, left, middle - 1, target)
        else:
            return self.binarySearch(nums, middle + 1, right, target)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        self.rows = len(matrix)
        self.cols = len(matrix[0])

        left = 0
        right = len(matrix) * len(matrix[0]) - 1
        
        return self.binarySearch(matrix, left, right, target)