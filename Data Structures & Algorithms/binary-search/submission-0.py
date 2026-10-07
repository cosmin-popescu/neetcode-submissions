class Solution:
    def binarySearch(self, nums, left, right, target):

        # we're done
        if left > right:
            return -1

        middle = (left + right) // 2

        # found it
        if target == nums[middle]:
            return middle

        # search to the left
        elif target < nums[middle]:
            return self.binarySearch(nums, left, middle - 1, target)

        # search to the right
        else:
            return self.binarySearch(nums, middle + 1, right, target) 

    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1 # assuming len > 0

        return self.binarySearch(nums, left, right, target)

        

