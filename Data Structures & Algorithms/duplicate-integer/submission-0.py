class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_table = {}
        for i in nums:
            if i not in hash_table:
                hash_table[i] = True
            else:
                return True
        return False