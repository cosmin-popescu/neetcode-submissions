class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ma_stack = []
        marea = 0

        for i, h in enumerate(heights):
            
            # if current bar h is smaller than the stack top,
            # this triggers a calculation for the rectangles
            # that can be formed with the previous (taller) bars
            while ma_stack and h < heights[ma_stack[-1]]:
                    pop = ma_stack.pop()
                    hpop = heights[pop]

                    # stack empty means bar can extend up to index i
                    # else it's bounded by the bar on the stack
                    if ma_stack:
                        width = i - ma_stack[-1] - 1
                    else:
                        width = i

                    # update max area
                    area = hpop * width
                    if area > marea:
                        marea = area

            # bar is taller than stack top, push it.
            ma_stack.append(i)   

        #cleanup:
        while ma_stack:
            pop = ma_stack.pop()
            hpop = heights[pop]
            if ma_stack:
                    width = len(heights) - ma_stack[-1] - 1
            else:
                width = len(heights)
            # update max area
            area = hpop * width
            if area > marea:
                marea = area
        return marea
            