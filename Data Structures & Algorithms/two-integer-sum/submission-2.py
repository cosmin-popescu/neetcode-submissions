class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}

        for i in range(0, len(nums)):
            complement = target - nums[i] # what we're looking for 
            if complement in index_map:
                return [index_map[complement], i]
            else:
                index_map[nums[i]] = i
        return []