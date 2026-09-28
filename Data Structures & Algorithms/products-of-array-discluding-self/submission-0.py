class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p_up = [1] * len(nums) # prefix products up to i [a*b*c...i)
        p_down = [1] * len(nums) # prefix products down to i [z*y*x*...i)
        p_res = [] * len(nums)

        for i in range(1, len(nums)):
            p_up[i] = p_up[i-1] * nums[i - 1] # compute forward
            p_down[i] = p_down[i-1] * nums[len(nums) - i] # compute backwards

        for i in range(0, len(nums)):
            p_res.append(p_up[i] * p_down[len(nums) - i - 1])
        
        return p_res