class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # XOR
        res = 0
        for i in nums:
            res = res ^ i
        return res