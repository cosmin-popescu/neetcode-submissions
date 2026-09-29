class Solution:
    def trap(self, height: List[int]) -> int:

        if len(height) < 3:
            return 0

        prefix_maxes = [0] * len(height)
        suffix_maxes = [0] * len(height)

        pref_max = 0
        for i in range(len(height)):
            prefix_maxes[i] = pref_max
            pref_max = max(pref_max, height[i])

        suff_max = 0
        for j in range(len(height) - 1, -1, -1):
            suffix_maxes[j] = suff_max
            suff_max = max(suff_max, height[j])

        water = 0
        for i in range(len(height)):
            current_index_water = min(prefix_maxes[i], suffix_maxes[i]) - height[i]
            if current_index_water > 0:
                water += current_index_water

        return water

        


            



