class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_water = 0

        while left < right:
            max_water = max(max_water, (right - left) * min(heights[left], heights[right]))
            # we advance over the smaller bar, as the maximum water would be smaller than the current
            if heights[left] < heights[right]:
                left +=1
            else:
                right -= 1
        
        return max_water
