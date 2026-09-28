class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_seq = 0

        # iterate all nums
        for i in nums_set:

            if i - 1 not in nums_set:

                # scout for nums smaller than k 
                k = i
                while True:
                    if k - 1 in nums_set:
                        k = k - 1
                    else:
                        break
                seq = [k]

                # build full sequence
                while True:
                    if k + 1 in nums_set:
                        k = k + 1
                        seq.append(k)
                    else:
                        break
                max_seq = max(max_seq, len(seq))

        return max_seq

            
