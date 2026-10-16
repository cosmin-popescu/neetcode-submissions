class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1

        # find the segment where the target might fit in
        # by searching for the pivot index
        while left < right:

            mid = (left + right) // 2
            
            # are these 2 in the same part?
            if nums[mid] > nums[right]:
                # means the pivot is in the other side
                left = mid + 1
            else:
                right = mid      

        pivot = left    
        left = 0
        right = len(nums) - 1
        
        if target >= nums[pivot] and target <= nums[right]:
            left = pivot
        else:
            right = pivot - 1

        while left <= right:
        
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1 

        return -1

            