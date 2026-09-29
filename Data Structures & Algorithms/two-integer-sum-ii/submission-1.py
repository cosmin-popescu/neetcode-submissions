class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            dasum = numbers[left] + numbers[right]

            if dasum == target:
                return [left + 1, right + 1]
            elif dasum > target:
                right -= 1
            else:
                left += 1
        
        return []
