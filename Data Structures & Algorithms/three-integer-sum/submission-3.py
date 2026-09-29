class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort da badboi - nlogn
        nums.sort()
        res = []

        #i + j + k = 0
        #i = -(j + k)
        target = 0

        while target < len(nums) - 2:

            if target > 0 and nums[target] == nums[target - 1]: # same target means same pairs again
                target += 1
                continue

            left = target + 1
            right = len(nums) - 1

            while left < right:
                sumsum = nums[left] + nums[right]
                
                if sumsum == -nums[target]:
                    res.append([nums[target], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif sumsum > -nums[target]:
                    right -= 1
                else:
                    left += 1
            
            target += 1
        
        return res

        

